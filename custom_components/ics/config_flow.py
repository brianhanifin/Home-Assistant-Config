""" config flow """
from homeassistant.core import callback
from homeassistant.helpers.entity import async_generate_entity_id
from homeassistant.components.sensor import ENTITY_ID_FORMAT
from homeassistant import config_entries
import voluptuous as vol
import logging

import datetime
from tzlocal import get_localzone
from icalendar import Calendar, Event
from .const import *
import traceback

_LOGGER = logging.getLogger(__name__)


@config_entries.HANDLERS.register(DOMAIN)
class IcsFlowHandler(config_entries.ConfigFlow):
	# Initial setup
	CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL
	VERSION = 1

	# called once the flow is started by the user
	def __init__(self):
		self._errors = {}

	# will be called by sending the form, until configuration is done
	async def async_step_user(self, user_input=None):   # pylint: disable=unused-argument
		self._errors = {}
		if user_input is not None:
			# there is user input, check and save if valid
			self._errors = check_data(user_input)
			if self._errors == {}:
				# valid, store and leave
				return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)
		# no user input, or error. Show form
		return self.async_show_form(step_id="user", data_schema=vol.Schema(create_form(user_input)), errors=self._errors)

	# TODO .. what is this good for?
	async def async_step_import(self, user_input):  # pylint: disable=unused-argument
		"""Import a config entry.
		Special type of import, we're not actually going to store any data.
		Instead, we're going to rely on the values that are in config file.
		"""
		if self._async_current_entries():
			return self.async_abort(reason="single_instance_allowed")

		return self.async_create_entry(title="configuration.yaml", data={})

	# call back to start the change flow
	@staticmethod
	@callback
	def async_get_options_flow(config_entry):
		return OptionsFlowHandler(config_entry)

# helper to validate user input
def check_data(user_input, own_id = None):
	ret = {}
	try:
		cal_string = load_data(user_input[CONF_ICS_URL])
		try:
			Calendar.from_ical(cal_string)
		except:
			_LOGGER.error(traceback.format_exc())
			ret["base"] = ERROR_ICS
			return ret
	except:
		_LOGGER.error(traceback.format_exc())
		ret["base"] = ERROR_URL
		return ret
	try:
		datetime.datetime.now(get_localzone()).strftime(user_input[CONF_TIMEFORMAT])
	except:
		_LOGGER.error(traceback.format_exc())
		ret["base"] = ERROR_TIMEFORMAT
		return ret
	if(user_input[CONF_ID]<0):
		_LOGGER.error("ICS: ID below zero")
		ret["base"] = ERROR_SMALL_ID
		return ret
	elif(user_input[CONF_LOOKAHEAD]<1):
		_LOGGER.error("ICS: Lookahead < 1")
		ret["base"] = ERROR_SMALL_LOOKAHEAD
		return ret
	
	if((own_id != user_input[CONF_ID]) and (get_hass() != None)):
		if(async_generate_entity_id(ENTITY_ID_FORMAT, "ics_" + str(user_input[CONF_ID]), hass=get_hass()) != PLATFORM+".ics_" + str(user_input[CONF_ID])):
			_LOGGER.error("ICS: ID not unique")
			ret["base"] = ERROR_ID_NOT_UNIQUE
			return ret
	return ret

class OptionsFlowHandler(config_entries.OptionsFlow):
	# change an entity via GUI
	def __init__(self, config_entry):
		# store old entry for later
		self.config_entry = config_entry
		self.own_id = config_entry.data[CONF_ID]

	# will be called by sending the form, until configuration is done
	async def async_step_init(self, user_input=None):
		self._errors = {}
		if user_input is not None:
			self._errors = check_data(user_input,self.own_id)
			if self._errors == {}:
				# title doesn't update .. :(
				return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)
		elif self.config_entry is not None:
			# if we came straight from init
			user_input = self.config_entry.data
			self.config_entry = None
		# form is created in const.py
		return self.async_show_form(step_id="init", data_schema=vol.Schema(create_form(user_input)), errors=self._errors)