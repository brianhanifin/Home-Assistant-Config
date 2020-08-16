"""Support for calendars based on entities."""
from datetime import datetime, time, timedelta
import logging

import voluptuous as vol

from homeassistant.components.calendar import PLATFORM_SCHEMA, CalendarEventDevice
from homeassistant.const import (
    CONF_ID, 
    CONF_NAME,
    CONF_TOKEN,
    STATE_UNKNOWN,
    STATE_UNAVAILABLE,
)
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.template import DATE_STR_FORMAT
from homeassistant.util import Throttle, dt

_LOGGER = logging.getLogger(__name__)

CONF_CALENDARS = "calendars"
CONF_CALENDAR_ENTITIES = "entities"
CONF_ENTITY = "entity"

CONF_START_TIME = "start_time"
CONF_END_TIME = "end_time"
CONF_TIMESTAMP_ATTRIBUTE = "timestamp_attribute"
CONF_TIMESTAMP_IN_STATE = "timestamp_in_state"
CONF_ALL_DAY = "all_day"

MSG_TIMESTAMP_CONFLICT = "Pass only one of timestamp_in_state or timestamp_attribute"

CALENDAR_ENTITY_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_ENTITY) : vol.All(vol.Lower, cv.string),
        vol.Optional(CONF_NAME): cv.string,
        vol.Optional(CONF_START_TIME, default={}) : vol.Schema(
            {
                vol.Exclusive(
                    CONF_TIMESTAMP_ATTRIBUTE,
                    CONF_START_TIME,
                    msg=MSG_TIMESTAMP_CONFLICT): cv.string,
                vol.Exclusive(
                    CONF_TIMESTAMP_IN_STATE,
                    CONF_START_TIME,
                    msg=MSG_TIMESTAMP_CONFLICT): cv.boolean
            }
        ),
        vol.Optional(CONF_END_TIME, default={}) : vol.Schema(
            {
                vol.Exclusive(
                    CONF_TIMESTAMP_ATTRIBUTE,
                    CONF_END_TIME,
                    msg=MSG_TIMESTAMP_CONFLICT): cv.string,
                vol.Exclusive(
                    CONF_TIMESTAMP_IN_STATE,
                    CONF_END_TIME,
                    msg=MSG_TIMESTAMP_CONFLICT): cv.boolean
            }
        ),
        vol.Optional(CONF_ALL_DAY) : cv.boolean,  
    }
)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_CALENDARS): vol.All(
            cv.ensure_list,
            vol.Schema(
                [
                    vol.Schema(
                        {
                            vol.Required(CONF_NAME): cv.string,
                            vol.Required(CONF_CALENDAR_ENTITIES): vol.All(
                                cv.ensure_list, [CALENDAR_ENTITY_SCHEMA]
                            )
                        }
                    )
                ]
            ),
        ),
    }
)

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=15)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the entities platform."""
    calendars = config[CONF_CALENDARS]
    calendar_devices = []
    
    for calendar in calendars:
        # Special filter: By date
        entities = calendar.get(CONF_CALENDAR_ENTITIES)

        # Create the calendar and add it to the devices array.
        calendar_devices.append(
            EntitiesCalendarDevice(
                hass,
                calendar,
                entities,
            )
        )

    add_entities(calendar_devices)


def _parse_date(date) -> datetime:
    """Parse the due date dict into a datetime object."""
    # Add time information to date only strings.
    if len(date) == 10:
        date += "T00:00:00"
    # If there is no timezone provided, use UTC.
    if not date.endswith("Z") and not "+" in date[11:] and not "-" in date[11:]:
        date += "Z"
    return dt.parse_datetime(date)

def _get_date(options, state_object):
    if state_object is None:
        return None

    timestamp_in_state = options.get(CONF_TIMESTAMP_IN_STATE, None)
    timestamp_attribute = options.get(CONF_TIMESTAMP_ATTRIBUTE, None)

    if timestamp_in_state is None:
        timestamp_in_state = (False if timestamp_attribute is not None else state_object.attributes.get("device_class") == "timestamp")

    if timestamp_in_state:
        if state_object.state == STATE_UNKNOWN or state_object.state == STATE_UNAVAILABLE:
            return None
        return _parse_date(state_object.state)
    else:
        if timestamp_attribute is None:
            return state_object.last_changed
        else:
            attribute_value = state_object.attributes.get(timestamp_attribute)
            if attribute_value is None or attribute_value == "":
                return None
            else:
                return _parse_date(attribute_value)

class EntitiesCalendarDevice(CalendarEventDevice):
    """A device for getting calendar events from entities."""

    def __init__(
        self,
        hass,
        calendar,
        entities,
    ):
        """Create the Todoist Calendar Event Device."""
        self.data = EntitiesCalendarData(
            hass,
            calendar,
            entities,
        )
        self._cal_data = {}
        self._name = calendar[CONF_NAME]

    @property
    def event(self):
        """Return the next upcoming event."""
        return self.data.event

    @property
    def name(self):
        """Return the name of the entity."""
        return self._name

    def update(self):
        """Update all Calendars."""
        self.data.update()


    async def async_get_events(self, hass, start_date, end_date):
        """Get all events in a specific time frame."""
        return await self.data.async_get_events(hass, start_date, end_date)

    @property
    def device_state_attributes(self):
        """Return the device state attributes."""
        if self.data.event is None:
            # No tasks, we don't REALLY need to show anything.
            return None

        return {}


class EntitiesCalendarData:
    """
    Class used by the Entities Calendar Device service object to hold all entity events.

    This is analogous to the GoogleCalendarData found in the Google Calendar
    component.

    The 'update' method polls for any updates to the entities. This is throttled to every
    MIN_TIME_BETWEEN_UPDATES minutes.
    """

    def __init__(
        self,
        hass,
        calendar,
        entities,
    ):
        """Initialize an Entities Calendar Project."""
        self.event = None

        self._hass = hass
        self._name = calendar[CONF_NAME]
        self._calendar = calendar
        self._entities = entities

        self.all_events = []


    async def async_get_events(self, hass, start_date, end_date):
        """Get all tasks in a specific time frame."""
        events = []
        for entity in self._entities:
            state_object = self._hass.states.get(entity[CONF_ENTITY])
            start = _get_date(entity[CONF_START_TIME], state_object)

            if start and not entity[CONF_END_TIME]:
                # If there is a start time and no end time options are defined
                # also use the start time as the end time
                end = start
            else:
                end = _get_date(entity[CONF_END_TIME], state_object)

            if start is None:
                continue

            if start_date < start < end_date:
                allDay = entity.get(CONF_ALL_DAY)
                if allDay is None:
                    # If this entity is not specifically identified as all day
                    # determine based on time being midnight
                    allDay = start.time() == time(0)

                event = {
                    "uid": entity,
                    "summary": entity.get(CONF_NAME, state_object.attributes.get("friendly_name")),
                    "start": { "date": start.strftime('%Y-%m-%d') } if allDay else { "dateTime": start.isoformat() },
                    "end": { "date": end.strftime('%Y-%m-%d') } if allDay else { "dateTime": end.isoformat() },
                    "allDay": allDay,
                }
                events.append(event)
        return events

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Get the latest data."""
        events = []
        for entity in self._entities:
            state_object = self._hass.states.get(entity[CONF_ENTITY])
            start = _get_date(entity[CONF_START_TIME], state_object)

            if start and not entity[CONF_END_TIME]:
                # If there is a start time and no end time options are defined
                # also use the start time as the end time
                end = start
            else:
                end = _get_date(entity[CONF_END_TIME], state_object)

            if start is None:
                continue

            allDay = entity.get(CONF_ALL_DAY)
            if allDay is None:
                # If this entity is not specifically identified as all day
                # determine based on time being midnight
                allDay = start.time() == time(0)

            event = {
                "uid": entity,
                "summary": entity.get(CONF_NAME, state_object.attributes.get("friendly_name")),
                "start": { "date": start.strftime('%Y-%m-%d') } if allDay else { "dateTime": start.isoformat() },
                "end": { "date": end.strftime('%Y-%m-%d') } if allDay else { "dateTime": end.isoformat() },
                "allDay": allDay,
            }
            events.append(event)

        events.sort(key=lambda x: x["start"]["date"] if x["allDay"] else x["start"]["dateTime"] )

        next_event = None
        if events:
          next_event = events[0]
        self.event = next_event
        _LOGGER.debug("Updated %s", self._name)