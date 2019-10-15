import logging
from datetime import datetime

from homeassistant.const import (CONF_ENTITY_ID, EVENT_STATE_CHANGED,
                                 EVENT_HOMEASSISTANT_START)
from homeassistant.helpers.event import track_time_interval
from homeassistant.helpers.dispatcher import dispatcher_send
from homeassistant.helpers.script import Script

from homeassistant.components.group import DOMAIN as GROUP_DOMAIN

from .const import *

_LOGGER = logging.getLogger(__name__)


class HomeAutomationManagerData:
    """The Class for handling the data retrieval."""

    def __init__(self, hass, scan_interval, configuration):
        """Initialize the data object."""
        _LOGGER.debug(f'HomeAutomationManagerData initialization with following configuration: {configuration}')

        self._profiles = configuration[CONF_PROFILES]
        self._events = configuration[CONF_EVENTS]
        self._trackers = configuration[CONF_TRACKERS]
        self._scenes = configuration[CONF_SCENES]
        self._custom_profiles = configuration[ATTR_CUSTOM_PROFILES]
        self._configuration_errors = configuration[ATTR_CONFIG_ERRORS]

        self._hass = hass
        self._was_initialized = False

        if self._configuration_errors is not None:
            log_message = '<br /> - '.join(self._configuration_errors)
            self.create_persistent_notification(log_message)
            return

        validations = [self.validate_scenes, self.validate_trackers]
        is_valid = True

        for validation in validations:
            if not validation():
                is_valid = False

        if is_valid:
            self._current_scene = None
            self._events_of_today = None
            self._latest_details = None
            self._current_date_time = None
            self._current_weekday = None
            self._current_part = None
            self._current_profile = None
            self._profile_data = None
            self._is_away = None
            self._group_trackers_id = None

            self.create_tracker_group()
            self.initialize_profile_data()

            def ham_refresh(event_time):
                """Call Home Automation Manager (HAM) to refresh information."""
                _LOGGER.debug(f'Updating Home Automation Manager (HAM) component, at {event_time}')
                self.update()
                dispatcher_send(hass, SIGNAL_UPDATE_HAM)

            def ham_run_current_scene(event_time):
                """Call Home Automation Manager (HAM) to run current scene."""
                _LOGGER.debug(f'Calling current scene script, at {event_time}')
                self.invoke_current_scene()

            self._ham_run_current_scene = ham_run_current_scene
            self._ham_refresh = ham_refresh

            def check_event(event):
                if event.data[CONF_ENTITY_ID] == self._group_trackers_id:
                    time_fired = event.time_fired

                    self._ham_refresh(time_fired)

            # register service
            hass.services.register(DOMAIN, 'update', ham_refresh)
            hass.services.register(DOMAIN, 'run_current_scene', ham_run_current_scene)

            # register scan interval for Home Automation Manager (HAM)
            track_time_interval(hass, ham_refresh, scan_interval)

            hass.bus.listen_once(EVENT_HOMEASSISTANT_START, ham_refresh)

            hass.bus.listen(EVENT_STATE_CHANGED, check_event)

            self._was_initialized = True

    def was_initialized(self):
        return self._was_initialized

    def create_persistent_notification(self, message):
        self._hass.components.persistent_notification.create(
            message,
            title=NOTIFICATION_TITLE,
            notification_id=NOTIFICATION_ID)

    def validate_scenes(self):
        if self._scenes is not None:
            for scene_key in self._scenes:
                scene = self._scenes[scene_key]
                scene_name = scene[CONF_SCENE_NAME]

                _LOGGER.debug(f'Validate Scene {scene_name}')

        return True

    def validate_trackers(self):
        if self._trackers is not None:
            for tracker in self._trackers:
                _LOGGER.debug(f'Validate Tracker {tracker}')

                current_tracker_domain = tracker.split('.')[0]

                if current_tracker_domain not in ALLOWED_TRACKERS:
                    self.create_persistent_notification(f'{tracker} is not supported tracker by HAM')

                    return False

        return True

    def create_tracker_group(self):
        group_trackers_id = f'{DOMAIN}_trackers'

        self._group_trackers_id = f'{GROUP_DOMAIN}.{group_trackers_id}'

        set_group_service = 'set'

        group_data = {
            'object_id': group_trackers_id,
            'icon': GROUP_TRACKER_ICON,
            'visible': True,
            'name': f'{DOMAIN.upper()} Trackers',
            'entities': self._trackers
        }

        self._hass.services.call(GROUP_DOMAIN, set_group_service, group_data, False)

    def get_current_date_time(self):
        return self._current_date_time

    def update_current_date_time(self):
        _LOGGER.debug("update_current_date_time - Start")

        self._current_date_time = datetime.now()

        _LOGGER.debug(f'update_current_date_time - Completed, Current date and time is {self._current_date_time}')

    def get_weekday(self):
        return self._current_weekday

    def update_weekday(self):
        _LOGGER.debug("update_weekday - Start")

        self._current_weekday = self._current_date_time.strftime('%A')

        _LOGGER.debug(f'update_weekday - Completed, today is {self._current_date_time}')

    def get_day_part(self):
        return self._current_part

    def update_day_part(self):
        try:
            _LOGGER.debug("update_day_part - Start")

            current_time = self._current_date_time.time()
            current_profile_name = self.get_current_profile()

            if current_profile_name not in self._profiles:
                _LOGGER.warning(f'update_day_part - failed to find profile {current_profile_name} in profiles')
            else:
                current_profile = self._profiles[current_profile_name]
                parts = current_profile[CONF_PARTS]

                _LOGGER.debug(f'update_day_part - Available Parts in {current_profile_name} JSON: {parts}')

                self._current_part = DAY_PART_TYPES[len(DAY_PART_TYPES) - 1]

                if parts is not None:
                    for part_name in parts:
                        part_from = parts[part_name]

                        part_from_time = datetime.strptime(part_from, "%H:%M:%S").time()

                        log_message = f'Checking {part_name} with from time {part_from_time} comparing {current_time}'
                        _LOGGER.debug(f'update_day_part - {log_message}')

                        if current_time >= part_from_time:
                            self._current_part = part_name

                _LOGGER.debug(f'update_day_part - Completed, Current day part is {self._current_part}')
        except Exception as ex:
            _LOGGER.error(f'updateDayPart - Error: {str(ex)}')

    def get_events_of_today(self):
        return self._events_of_today

    def get_events_of_today_titles(self):
        title = None
        try:
            titles = []

            if self._events_of_today is not None:
                for event in self._events_of_today:
                    titles.append(f'{event[CONF_EVENT_TITLE]} ({event[CONF_PROFILE_NAME]})')

            title = ', '.join(titles)
        except Exception as ex:
            _LOGGER.error(f'getEventsOfTodayTitles - Exception {str(ex)}')

        return title

    def update_events_of_today(self):
        try:

            events = self._events

            if events is None:
                _LOGGER.debug("update_events_of_today - No overrides available")

                return
            else:
                _LOGGER.debug(f'update_events_of_today - Start, Available overrides are: {events}')

            self._events_of_today = []

            current_date = self._current_date_time.today().strftime('%Y-%m-%d')
            _LOGGER.debug(f'update_events_of_today - Today is {current_date}')

            current_day_name = self.get_weekday()

            for main_event_key in events:
                main_event = events[main_event_key]
                for event in main_event:
                    event_profile = event[CONF_PROFILE_NAME]
                    event_title = event[CONF_EVENT_TITLE]

                    log_message = f'Event {event_title} profile {event_profile} is'

                    if main_event_key in [current_day_name, current_date]:
                        log_message = f''
                        _LOGGER.debug(f'update_events_of_today - {log_message} from today ({main_event_key})')
                        self._events_of_today.append(event)
                    else:
                        _LOGGER.debug(f'update_events_of_today - {log_message} not from today ({main_event_key})')

            _LOGGER.debug("update_events_of_today - Completed")
        except Exception as ex:
            _LOGGER.error(f'update_events_of_today - Error {str(ex)}')

    def get_current_scene(self):
        return self._current_scene

    def update_current_scene(self):
        is_away = self.get_is_away()
        current_scene = self.get_day_part()

        if is_away:
            current_scene = AWAY_PROFILE

        self._current_scene = current_scene

    def get_profile_data(self, profile):
        profile_data_all = {}

        if self._profile_data is not None and profile in self._profile_data:
            profile_data = self._profile_data[profile]

            if ATTR_PARTS_EVENTS in profile_data:
                profile_data_all = profile_data[ATTR_PARTS_EVENTS]

        return profile_data_all

    def get_current_profile_data_parts(self):
        profile = self.get_current_profile()

        profile_data_parts = {}

        if self._profile_data is not None and profile in self._profile_data:
            profile_data = self._profile_data[profile]
            if ATTR_PARTS in profile_data:
                profile_data_parts = profile_data[ATTR_PARTS]

        return profile_data_parts

    def initialize_profile_data(self):
        self._profile_data = {}

        all_profiles = self.get_profiles()

        _LOGGER.debug('Loading HAM Binary Sensors')

        for profile_name in all_profiles:
            profile = all_profiles[profile_name]
            parts = None
            events = None

            self._profile_data[profile_name] = {
                ATTR_PARTS_EVENTS: {},
                ATTR_PARTS: {}
            }

            profile_data_all = self._profile_data[profile_name][ATTR_PARTS_EVENTS]
            profile_data_parts = self._profile_data[profile_name][ATTR_PARTS]

            if CONF_PARTS in profile:
                parts = profile[CONF_PARTS]

            if CONF_EVENTS in profile:
                events = profile[CONF_EVENTS]

            if parts is not None:
                for part_name in parts:
                    value = parts[part_name]

                    profile_data_all[part_name] = value
                    profile_data_parts[part_name] = value

            if events is not None:
                for event_id in events:
                    event = events[event_id]
                    event_title = event[CONF_EVENT_TITLE]
                    event_id_arr = event_id.split('.')
                    event_date = event_id_arr[len(event_id_arr) - 1]

                    profile_data_all[event_title] = event_date

    def get_current_profile(self):
        return self._current_profile

    def update_current_profile(self):
        try:
            _LOGGER.debug("update_current_profile - Start")

            self._current_profile = DEFAULT_PROFILE
            events = self.get_events_of_today()

            if events is not None:
                for event in events:
                    event_profile = event[CONF_PROFILE_NAME]

                    if self._current_profile != self._custom_profiles[len(self._custom_profiles) - 1]:
                        self._current_profile = event_profile

            _LOGGER.debug(f'update_current_profile - Completed, Profile of today is {self._current_profile}')
        except Exception as ex:
            _LOGGER.error(f'update_current_profile - Error: {str(ex)}')

    def get_details(self):
        return self._latest_details

    def get_profiles(self):
        return self._profiles

    def get_is_away(self):
        return self._is_away

    def update_is_away(self):
        try:
            _LOGGER.debug("update_is_away - Start")

            group_tracker_state = self._hass.states.get(self._group_trackers_id).state

            self._is_away = group_tracker_state in TRACKERS_AWAY_STATES

            _LOGGER.debug(f'update_is_away - Completed, Away state is {self._is_away}')
        except Exception as ex:
            _LOGGER.error(f'update_is_away - Error: {str(ex)}')

    def invoke_current_scene(self):
        current_scene = self.get_current_scene()

        _LOGGER.debug(f'Invoking script of {current_scene}')

        if self._scenes is not None and current_scene in self._scenes:
            scene = self._scenes[current_scene]

            if CONF_SCENE_SCRIPT in scene:
                scene_script = scene[CONF_SCENE_SCRIPT]

                if scene_script is not None:
                    script_invoker = Script(self._hass, scene_script)
                    script_invoker.run()

    def update(self):
        _LOGGER.debug("update - Start")

        current_scene = self.get_current_scene()

        self.update_current_date_time()
        self.update_weekday()
        self.update_events_of_today()
        self.update_is_away()
        self.update_current_profile()
        self.update_day_part()
        self.update_current_scene()

        if current_scene is not None and current_scene != self.get_current_scene():
            self.invoke_current_scene()

        _LOGGER.debug("update - Completed")
