"""The Logbook Cache monkey integration."""
import asyncio
import threading
import datetime
import logging

from homeassistant.core import callback
import homeassistant.components.logbook as lb
import homeassistant.helpers.config_validation as cv
import homeassistant.util.dt as dt_util

from .const import DOMAIN, CACHE_DAYS, DEFAULT_CACHE_DAYS

_LOGGER = logging.getLogger(__name__)

monkey = None
logbook_config = None


async def async_setup(hass, config):
    global logbook_config
    logbook_config = config.get(lb.DOMAIN, {})

    return True


async def async_setup_entry(hass, entry):
    global monkey
    monkey = MonkeyClass(hass, entry)
    monkey.async_start()

    entry.add_update_listener(async_update_listener)

    return True


async def async_unload_entry(hass, entry):
    global monkey
    monkey.async_stop()
    monkey = None

    return True


async def async_update_listener(hass, entry):
    monkey.async_update_listener()


def step_timestamp(timestamp):
    return timestamp + datetime.timedelta(minutes=lb.GROUP_BY_MINUTES)


class MonkeyClass:
    def __init__(self, hass, config_entry):
        self.hass = hass
        self.cache = {}
        self.load_lock = threading.Lock()
        self.async_refresh_unsub = None
        self.config_entry = config_entry
        self.original_get_events = None

    def async_start(self):
        self.original_get_events = lb._get_events
        lb._get_events = self.wrap_get_events

        self.async_refresh_unsub = self.hass.helpers.event.async_call_later(
            30, self.async_refresh_cache
        )

    def async_stop(self):
        if self.async_refresh_unsub:
            self.async_refresh_unsub()
            self.async_refresh_unsub = None

        self.cache = {}

        lb._get_events = self.original_get_events

    @callback
    def async_update_listener(self):
        cache_days = self.config_entry.options.get(CACHE_DAYS, DEFAULT_CACHE_DAYS)
        _LOGGER.debug(f"cache_days={cache_days}")

        if self.async_refresh_unsub:
            self.async_refresh_unsub()
            self.async_refresh_unsub = None

        self.async_refresh_cache()

    def wrap_get_events(self, hass, logbook_config, start_day, end_day, entity_id=None):
        if entity_id is not None or end_day <= self.cache_start():
            _LOGGER.debug(f"Forwarding for {start_day}-{end_day}")
            return self.original_get_events(
                hass, logbook_config, start_day, end_day, entity_id
            )

        events = []

        timestamp = start_day
        with self.load_lock:
            while timestamp < end_day:
                events.extend(self.load_chunk(timestamp))
                timestamp = step_timestamp(timestamp)

        return events

    def cache_start(self):
        cache_days = self.config_entry.options.get(CACHE_DAYS, DEFAULT_CACHE_DAYS)

        return dt_util.as_utc(
            dt_util.start_of_local_day() - datetime.timedelta(days=cache_days - 1)
        )

    @callback
    def async_refresh_cache(self, now=None):
        def refresh():
            start = self.cache_start()

            with self.load_lock:
                _LOGGER.debug(f"Purging until {start}")
                for key in list(self.cache.keys()):
                    if key < start:
                        _LOGGER.debug(f"Removing {key}")
                        del self.cache[key]

            _LOGGER.debug(f"Caching from {start}")
            refresh = []
            timestamp = start
            while step_timestamp(timestamp) < dt_util.utcnow():
                refresh.append(timestamp)
                timestamp = step_timestamp(timestamp)

            for timestamp in reversed(refresh):
                with self.load_lock:
                    self.load_chunk(timestamp)

        current_timestamp = dt_util.as_utc(dt_util.start_of_local_day())
        while step_timestamp(current_timestamp) < dt_util.utcnow():
            current_timestamp = step_timestamp(current_timestamp)

        _LOGGER.debug(f"Scheduling fill of {current_timestamp}")
        self.async_refresh_unsub = self.hass.helpers.event.async_track_point_in_utc_time(
            self.async_refresh_cache, step_timestamp(current_timestamp)
        )

        self.hass.async_add_executor_job(refresh)

    def load_chunk(self, timestamp):
        if timestamp in self.cache:
            return self.cache[timestamp]

        if timestamp > dt_util.utcnow():
            return []

        _LOGGER.debug(f"Loading {timestamp}")
        next_timestamp = step_timestamp(timestamp)
        chunk = self.original_get_events(
            self.hass, logbook_config, timestamp, next_timestamp
        )

        if self.cache_start() <= timestamp and next_timestamp < dt_util.utcnow():
            _LOGGER.debug(f"Storing {timestamp}")
            self.cache[timestamp] = chunk

        return chunk
