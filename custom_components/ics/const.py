from homeassistant.components.sensor import PLATFORM_SCHEMA, ENTITY_ID_FORMAT
from homeassistant.helpers.entity import async_generate_entity_id
import homeassistant.helpers.config_validation as cv
from homeassistant.const import (CONF_NAME)
import voluptuous as vol


from collections import OrderedDict
import logging
from homeassistant.core import callback
from homeassistant import config_entries

from urllib.request import urlopen, Request

# generals
ICON = 'mdi:calendar'
DOMAIN = "ics"
PLATFORM = "sensor"
VERSION = "1.0.0"
ISSUE_URL = "https://github.com/koljawindeler/ics/issues"

# configuration
CONF_ICS_URL = "url"
CONF_NAME = "name"
CONF_ID = "id"
CONF_TIMEFORMAT = "timeformat"
CONF_LOOKAHEAD = "lookahead"
CONF_SW = "startswith"
CONF_SHOW_BLANK = "show_blank"
CONF_FORCE_UPDATE = "force_update"
CONF_SHOW_REMAINING = "show_remaining"
CONF_SHOW_ONGOING = "show_ongoing"

# defaults
DEFAULT_NAME = "ics_sensor"
DEFAULT_SW = ""
DEFAULT_ID = 1
DEFAULT_TIMEFORMAT = "%A, %d.%m.%Y"
DEFAULT_LOOKAHEAD = 365
DEFAULT_SHOW_BLANK = ""
DEFAULT_FORCE_UPDATE = 0
DEFAULT_SHOW_REMAINING = True
DEFAULT_SHOW_ONGOING = False

# error 
ERROR_URL = "invalid_url"
ERROR_ICS = "invalid_ics"
ERROR_TIMEFORMAT = "invalid_timeformat"
ERROR_SMALL_ID = "invalid_small_id"
ERROR_SMALL_LOOKAHEAD = "invalid_lookahead"
ERROR_ID_NOT_UNIQUE = "id_not_unique"

# extend schema to load via YAML
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
	vol.Required(CONF_ICS_URL): cv.string,
	vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
	vol.Optional(CONF_ID, default=DEFAULT_ID): vol.Coerce(int),
	vol.Optional(CONF_TIMEFORMAT, default=DEFAULT_TIMEFORMAT): cv.string,
	vol.Optional(CONF_SW, default=DEFAULT_SW): cv.string,
	vol.Optional(CONF_LOOKAHEAD, default=DEFAULT_LOOKAHEAD): vol.Coerce(int),
	vol.Optional(CONF_SHOW_BLANK, default=DEFAULT_SHOW_BLANK): cv.string,
	vol.Optional(CONF_FORCE_UPDATE, default=DEFAULT_FORCE_UPDATE): vol.Coerce(int),
	vol.Optional(CONF_SHOW_REMAINING, default=DEFAULT_SHOW_REMAINING): cv.boolean,
	vol.Optional(CONF_SHOW_ONGOING, default=DEFAULT_SHOW_ONGOING): cv.boolean,
})

myhass = []
def store_hass(hass):
	myhass.append(hass)

def get_hass():
	if not myhass:
		return None
	return myhass[0]

def get_next_id():
	for i in range(1,999):
		if(async_generate_entity_id(ENTITY_ID_FORMAT, "ics_" + str(i), hass=get_hass()) == PLATFORM+".ics_" + str(i)):
			return i
	return 999

# create form for UI setup
def create_form(user_input):
	name = ""
	url = ""
	timeformat = DEFAULT_TIMEFORMAT
	starts_with = DEFAULT_SW
	lookahead = DEFAULT_LOOKAHEAD
	show_blank =  DEFAULT_SHOW_BLANK
	force_update =  DEFAULT_FORCE_UPDATE
	show_remaining = DEFAULT_SHOW_REMAINING
	show_ongoing = DEFAULT_SHOW_ONGOING

	# generate next available ID
	id = get_next_id()

	if user_input is not None:
		if CONF_NAME in user_input:
			name = user_input[CONF_NAME]
		if CONF_ICS_URL in user_input:
			url = user_input[CONF_ICS_URL]
		if CONF_ID in user_input:
			id = user_input[CONF_ID]
		if CONF_TIMEFORMAT in user_input:
			timeformat = user_input[CONF_TIMEFORMAT]
		if CONF_SW in user_input:
			starts_with = user_input[CONF_SW]
			if(starts_with==" "):
				starts_with = ""
		if CONF_LOOKAHEAD in user_input:
			lookahead = user_input[CONF_LOOKAHEAD]
		if CONF_SHOW_REMAINING in user_input:
			show_remaining = user_input[CONF_SHOW_REMAINING]
		if CONF_SHOW_BLANK in user_input:
			show_blank = user_input[CONF_SHOW_BLANK]
			if(show_blank == " "):
				show_blank = ""
		if CONF_FORCE_UPDATE in user_input:
			force_update = user_input[CONF_FORCE_UPDATE]

	data_schema = OrderedDict()
	data_schema[vol.Required(CONF_NAME, default = name)] = str
	data_schema[vol.Required(CONF_ICS_URL, default = url)] = str
	data_schema[vol.Required(CONF_ID, default = id)] = int
	data_schema[vol.Optional(CONF_TIMEFORMAT, default = timeformat)] = str
	data_schema[vol.Optional(CONF_SW, default = starts_with)] = str
	data_schema[vol.Optional(CONF_LOOKAHEAD, default = lookahead)] = int
	data_schema[vol.Optional(CONF_SHOW_BLANK, default = show_blank)] = str
	data_schema[vol.Optional(CONF_FORCE_UPDATE, default = force_update)] = int
	data_schema[vol.Optional(CONF_SHOW_REMAINING, default = show_remaining)] = bool
	data_schema[vol.Optional(CONF_SHOW_ONGOING, default = show_ongoing)] = bool
	return data_schema

# load data from URL, exported to const to call it from sensor and from config_flow
def load_data(url):
	req = Request(url=url, data=None, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
	return urlopen(req).read().decode('ISO-8859-1')
