import voluptuous as vol

from homeassistant.components.device_tracker import DOMAIN as DEVICE_TRACKER_DOMAIN
from homeassistant.const import (CONF_NAME, STATE_OFF, STATE_NOT_HOME)
from homeassistant.helpers import config_validation as cv

from datetime import timedelta

VERSION = '1.0.5'

DOMAIN = 'ham'
DATA_HAM = 'data_ham'
SIGNAL_UPDATE_HAM = "ham_update"
DEFAULT_NAME = 'Home Automation Manager'

GROUP_TRACKER_ICON = 'mdi:home'

ATTR_WEEKDAY = 'Weekday'
ATTR_DATE = 'Date'
ATTR_PROFILE = 'Profile'
ATTR_PARTS_EVENTS = 'Parts_Events'
ATTR_PARTS = 'Parts'
ATTR_PART = 'Part'
ATTR_EVENTS = 'Overrides of Today'
ATTR_CUSTOM_PROFILES = 'custom_profiles'
ATTR_CONFIG_ERRORS = 'configuration_errors'

DEFAULT_PROFILE = 'Default'
AWAY_PROFILE = 'Away'

DAY_PART_MORNING = 'Morning'
DAY_PART_NOON = 'Noon'
DAY_PART_AFTERNOON = 'Afternoon'
DAY_PART_EVENING = 'Evening'
DAY_PART_NIGHT = 'Night'

DAY_SUNDAY = 'Sunday'
DAY_MONDAY = 'Monday'
DAY_TUESDAY = 'Tuesday'
DAY_WEDNESDAY = 'Wednesday'
DAY_THURSDAY = 'Thursday'
DAY_FRIDAY = 'Friday'
DAY_SATURDAY = 'Saturday'

CONF_PARTS = 'parts'

CONF_PROFILES = 'profiles'
CONF_PROFILE_NAME = 'profile'
CONF_PROFILE_DEFAULT = 'default_profile'
CONF_PROFILE_FROM = 'from'

CONF_EVENTS = 'events'
CONF_EVENT_DATE = 'date'
CONF_EVENT_TIME = 'time'
CONF_EVENT_TITLE = 'title'
CONF_EVENT_DAY = 'day'

CONF_TRACKERS = 'trackers'
CONF_SCENES = 'scenes'
CONF_SCENE_NAME = 'scene'
CONF_SCENE_SCRIPT = 'script'

NOTIFICATION_ID = 'ham_notification'
NOTIFICATION_TITLE = 'Home Automation Manager Setup'

SCAN_INTERVAL = timedelta(seconds=60)

TRACKERS_AWAY_STATES = [STATE_NOT_HOME, STATE_OFF]
ALLOWED_TRACKERS = [DEVICE_TRACKER_DOMAIN]
SYSTEM_PROFILES = [DEFAULT_PROFILE, AWAY_PROFILE]
DAY_PART_TYPES = [DAY_PART_MORNING, DAY_PART_NOON, DAY_PART_AFTERNOON, DAY_PART_EVENING, DAY_PART_NIGHT]
DAY_NAMES = [DAY_SUNDAY, DAY_MONDAY, DAY_TUESDAY, DAY_WEDNESDAY, DAY_THURSDAY, DAY_FRIDAY, DAY_SATURDAY]
SCENES_TYPES = [DAY_PART_MORNING, DAY_PART_NOON, DAY_PART_AFTERNOON, DAY_PART_EVENING, DAY_PART_NIGHT, AWAY_PROFILE]

BINARY_SENSOR_DEFAULT_ICON = 'pig'
BINARY_SENSOR_DEFAULT_DEVICE_CLASS = 'None'

SENSOR_DEFAULT_ICON = 'ham'
SENSOR_DEFAULT_DEVICE_CLASS = 'None'

ATTR_DAY_PART = 'day_part'
ATTR_CURRENT_PROFILE = 'current_profile'
ATTR_CURRENT_SCENE = 'current_scene'
ATTR_STATE = 'state'
ATTR_ATTRIBUTES = 'attributes'

SENSOR_TYPES = {
    ATTR_WEEKDAY: ['Weekday', None, 'calendar-week-begin'],
    ATTR_DAY_PART: ['Current Day Part', None, 'weather-night'],
    ATTR_CURRENT_PROFILE: ['Current Profile', None, 'bullseye-arrow'],
    ATTR_CURRENT_SCENE: ['Current Scene', None, 'movie']
}

SCENE_SCHEMA = vol.Schema({
    vol.Required(CONF_SCENE_NAME):
        vol.In(SCENES_TYPES),
    vol.Optional(CONF_SCENE_SCRIPT): cv.SCRIPT_SCHEMA
})

PART_SCHEMA = vol.Schema({
    vol.Required(CONF_NAME):
        vol.In(DAY_PART_TYPES),
    vol.Required(CONF_PROFILE_FROM): cv.string,
})

PARTS_SCHEMA = vol.All(
    cv.ensure_list,
    [vol.Any(PART_SCHEMA)],
)

PROFILE_DEFAULT_SCHEMA = vol.Schema({
    vol.Required(CONF_PARTS): PARTS_SCHEMA
})

PROFILE_SCHEMA = vol.Schema({
    vol.Required(CONF_PROFILE_NAME): cv.string,
    vol.Required(CONF_PARTS):
        vol.All(cv.ensure_list, [vol.Any(PART_SCHEMA)])
})

PROFILE_OVERRIDE_SCHEMA = vol.Schema({
    vol.Required(CONF_PROFILE_NAME): cv.string,
    vol.Required(CONF_EVENT_TITLE): cv.string,
})

PROFILE_DATE_OVERRIDE_SCHEMA = PROFILE_OVERRIDE_SCHEMA.extend({
    vol.Required(CONF_EVENT_DATE): cv.string,
})

PROFILE_DAY_OVERRIDE_SCHEMA = PROFILE_OVERRIDE_SCHEMA.extend({
    vol.Required(CONF_EVENT_DAY):
        vol.In(DAY_NAMES),
})

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_PROFILE_DEFAULT): PROFILE_DEFAULT_SCHEMA,
        vol.Optional(CONF_PROFILES):
            vol.All(cv.ensure_list, [vol.Any(PROFILE_SCHEMA)]),
        vol.Optional(CONF_EVENTS):
            vol.All(cv.ensure_list, [vol.Any(PROFILE_DATE_OVERRIDE_SCHEMA, PROFILE_DAY_OVERRIDE_SCHEMA)]),
        vol.Optional(CONF_TRACKERS): cv.entity_ids,
        vol.Optional(CONF_SCENES):
            vol.All(cv.ensure_list, [vol.Any(SCENE_SCHEMA)]),
    }),
}, extra=vol.ALLOW_EXTRA)
