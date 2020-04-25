"""
@ Author	  : Kolja Windeler
@ Date		  : 06/02/2020
@ Description : Grabs an ics file and finds next event
@ Notes:		Copy this file and place it in your
				"Home Assistant Config folder\custom_components\sensor\" folder.
"""
import asyncio
import logging
import unicodedata

import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity, async_generate_entity_id
from homeassistant.components.sensor import PLATFORM_SCHEMA, ENTITY_ID_FORMAT
from homeassistant.const import (CONF_NAME)


from icalendar import Calendar, Event
from tzlocal import get_localzone
import recurring_ical_events
import datetime
import traceback

_LOGGER = logging.getLogger(__name__)

from .const import *

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
	_LOGGER.debug("Config via YAML")
	#_LOGGER.debug((config)
	if(config!=None):
		async_add_entities([ics_Sensor(hass, config)], True)

async def async_setup_entry(hass, config, async_add_devices):
	_LOGGER.debug("Config via Storage/UI")
	#_LOGGER.debug((config.data)
	if(len(config.data)>0):
		async_add_devices([ics_Sensor(hass, config.data)], True)

class ics_Sensor(Entity):
	"""Representation of a Sensor."""
	def __init__(self,hass, config):
		"""Initialize the sensor."""
		self._state_attributes = None
		self._state = None

		self._url = config.get(CONF_ICS_URL)
		self._name = config.get(CONF_NAME)
		self._sw = config.get(CONF_SW)
		self._timeformat = config.get(CONF_TIMEFORMAT)
		self._lookahead = config.get(CONF_LOOKAHEAD)
		self._show_blank = config.get(CONF_SHOW_BLANK)
		self._force_update = config.get(CONF_FORCE_UPDATE)
		self._show_remaining = config.get(CONF_SHOW_REMAINING)
		self._show_ongoing = config.get(CONF_SHOW_ONGOING)

		_LOGGER.debug("ICS config: ")
		_LOGGER.debug("\tname: "+self._name)
		_LOGGER.debug("\tID: "+str(config.get(CONF_ID)))
		_LOGGER.debug("\turl: "+self._url)
		_LOGGER.debug("\tsw: "+self._sw)
		_LOGGER.debug("\ttimeformat: "+self._timeformat)
		_LOGGER.debug("\tlookahead: "+str(self._lookahead))
		_LOGGER.debug("\tshow_blank: "+str(self._show_blank))
		_LOGGER.debug("\tforce_update: "+str(self._force_update))
		_LOGGER.debug("\tshow_remaining: "+str(self._show_remaining))
		_LOGGER.debug("\tshow_ongoing: "+str(self._show_ongoing))

		self._lastUpdate = -1
		self.ics = {
			'extra':{
				'start':None,
				'end':None,
				'remaining':-1,
				'description':"-",
				'location': '-',
				'last_updated': None,
				},
			'pickup_date': "-",
			}

		self.entity_id = async_generate_entity_id(ENTITY_ID_FORMAT, "ics_" + str(config.get(CONF_ID)), hass=hass)
	@property
	def name(self):
		"""Return the name of the sensor."""
		return self._name

	@property
	def device_state_attributes(self):
		"""Return the state attributes."""
		return self._state_attributes

	@property
	def state(self):
		"""Return the state of the sensor."""
		return self._state

	@property
	def icon(self):
		"""Return the icon to use in the frontend."""
		return ICON

	def fix_text(self,s):
		s=''.join(e for e in s if (e.isalnum() or e==' '))
		s = s.replace(chr(195), 'u')
		s = s.replace(chr(188), 'e')
		return s

	def exc(self):
		_LOGGER.error("\n\n============= ICS Integration Error ================")
		_LOGGER.error("unfortunately ICS hit an error, please open a ticket at")
		_LOGGER.error("https://github.com/KoljaWindeler/ics/issues")
		_LOGGER.error("and paste the following output:\n")
		_LOGGER.error(traceback.format_exc())
		_LOGGER.error("\nthanks, Kolja")
		_LOGGER.error("============= ICS Integration Error ================\n\n")

	# make sure all elements are timezone aware datetimes
	def check_fix_date_tz(self, event):
		if(isinstance(event.dt, datetime.date)):
			event.dt = datetime.datetime(event.dt.year,event.dt.month,event.dt.day)
		try:
			if(event.dt.tzinfo == None or event.dt.utcoffset() == None):
				event.dt = event.dt.replace(tzinfo=get_localzone())
		except:
			pass
		return event

	# make sure that the UNITL date of the RRULE is the same type as DTSTART is, otherwise recurring_ical_events will crash
	def check_fix_rrule(self,calendar):
		fix=0
		for event in calendar.walk('vevent'):
			if(event.has_key("RRULE")):
				if(event["RRULE"].has_key("UNTIL")):
					if(isinstance(event["DTSTART"].dt,datetime.date) and isinstance(event["RRULE"]["UNTIL"][0],datetime.datetime)):
						event["RRULE"]["UNTIL"][0] = event["RRULE"]["UNTIL"][0].date()
						fix+=1
					elif(isinstance(event["DTSTART"].dt,datetime.datetime) and isinstance(event["RRULE"]["UNTIL"][0],datetime.date)):
						fix+=1
						d = event["RRULE"]["UNTIL"][0]
						event["RRULE"]["UNTIL"][0] =  datetime.datetime(d.year,d.month,d.day)
						if(event["DTSTART"].dt.tzinfo != None):
							event["RRULE"]["UNTIL"][0] = event["RRULE"]["UNTIL"][0].replace(tzinfo=event["DTSTART"].dt.tzinfo)
		return fix


	def get_data(self):
		try:
			cal_string = load_data(self._url)
			cal = Calendar.from_ical(cal_string)

			# fix RRULE
			_LOGGER.debug(f"fixed {self.check_fix_rrule(cal)} RRule dates")
			
			# define calendar range
			start_date = datetime.datetime.now().replace(minute=0, hour=0, second=0, microsecond=0)
			end_date = start_date + datetime.timedelta(days=self._lookahead)

			reoccuring_events = recurring_ical_events.of(cal).between(start_date, end_date)

			# make all item TZ aware datetime
			for event in reoccuring_events:
				if(event.has_key("DTSTART")):
					event["DTSTART"] = self.check_fix_date_tz(event["DTSTART"])
				if(event.has_key("DTEND")):
					event["DTEND"] = self.check_fix_date_tz(event["DTEND"])
	
			try:
				reoccuring_events = sorted(reoccuring_events, key=lambda x: x["DTSTART"].dt, reverse=False)
			except:
				self.exc()

			et = None
			self.ics['pickup_date'] = "no next event"
			self.ics['extra']['last_updated'] = datetime.datetime.now(get_localzone()).replace(microsecond=0)
			self.ics['extra']['start'] = None
			self.ics['extra']['end'] = None
			self.ics['extra']['remaining'] = -1
			self.ics['extra']['description'] = "-"
			self.ics['extra']['location'] = "-"

			if(len(reoccuring_events)>0):
				for e in reoccuring_events:
					event_date = e["DTSTART"].dt
					if(e.has_key("DTEND")):
						event_end_date = e["DTEND"].dt
					else:
						event_end_date = event_date

					event_summary = ""
					if(e.has_key("SUMMARY")):
						event_summary = self.fix_text(e["SUMMARY"])
					elif(self._show_blank):
						event_summary = self.fix_text(self._show_blank)

					now = datetime.datetime.now(get_localzone())

					if(event_summary):
						if(event_summary.startswith(self.fix_text(self._sw))):
							if((event_date > now) or (self._show_ongoing and event_end_date > now)):
								if(et == None):
									self.ics['pickup_date'] = event_date.strftime(self._timeformat)
									self.ics['extra']['remaining'] = (event_date.date() - now.date()).days
									self.ics['extra']['description'] = event_summary
									self.ics['extra']['start'] = event_date
									self.ics['extra']['end'] = event_end_date
									if(e.has_key("LOCATION")):
										self.ics['extra']['location'] = self.fix_text(e["LOCATION"])
									et = event_date
								elif(event_date == et):
									self.ics['extra']['description'] += " / " + event_summary
									if(e.has_key("LOCATION")):
										self.ics['extra']['location'] += " / " + self.fix_text(e["LOCATION"])
									# store earliest end time
									if(self.ics['extra']['end'] > e["DTEND"].dt):
										self.ics['extra']['end'] = e["DTEND"].dt
								else:
									break
		except:
			self.ics['pickup_date'] = "failure"
			self.exc()


	def update(self):
		"""Fetch new state data for the sensor.
		This is the only method that should fetch new data for Home Assistant.
		"""
		try:
			# first run
			if(self.ics['extra']['last_updated']==None):
				self.get_data()

			# update at midnight
			elif(self.ics['extra']['last_updated'].day != datetime.datetime.now().day):
				self.get_data()

			# update if datetime exists (there was an event in reach) and it is past now (look for the next event)
			if(self.ics['extra']['start']!=None):
				if(self._show_ongoing):
					if(self.ics['extra']['end']<datetime.datetime.now(get_localzone())):
						self.get_data()
				else:
					if(self.ics['extra']['start']<datetime.datetime.now(get_localzone())):
						self.get_data()

			# force updates (this should be last in line to avoid running twice)
			if(self.ics['extra']['last_updated']!=None and self._force_update>0):
				if(self.ics['extra']['last_updated']+datetime.timedelta(seconds=self._force_update) < datetime.datetime.now(get_localzone())):
					self.get_data()

			# update states
			self._state_attributes = self.ics['extra']
			self._state = self.ics['pickup_date']
			if(self._show_remaining):
				self._state += ' (%02i)' % self.ics['extra']['remaining']
		except:
			self._state = "error"
			self.exc()
