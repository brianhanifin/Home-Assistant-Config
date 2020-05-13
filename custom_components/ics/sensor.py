"""
Custom component to grab ICS files.

@ Author	  : Kolja Windeler
@ Date		  : 06/02/2020
@ Description : Grabs an ics file and finds next event
@ Notes:		Copy this file and place it in your
				"Home Assistant Config folder\\custom_components\\sensor\" folder.
"""
import logging
from homeassistant.helpers.entity import Entity, async_generate_entity_id
from homeassistant.components.sensor import ENTITY_ID_FORMAT
from homeassistant.const import (CONF_NAME)


from icalendar import Calendar
from tzlocal import get_localzone
import recurring_ical_events
import datetime
import traceback
from .const import *

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
	"""Run setup via YAML."""
	_LOGGER.debug("Config via YAML")
	if(config is not None):
		async_add_entities([ics_Sensor(hass, config)], True)


async def async_setup_entry(hass, config, async_add_devices):
	"""Run setup via Storage."""
	_LOGGER.debug("Config via Storage/UI")
	if(len(config.data) > 0):
		async_add_devices([ics_Sensor(hass, config.data)], True)


class ics_Sensor(Entity):
	"""Representation of a Sensor."""

	def __init__(self, hass, config):
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
		self._group_events = config.get(CONF_GROUP_EVENTS)
		self._n_skip = config.get(CONF_N_SKIP)
		self._description_in_state = config.get(CONF_DESCRIPTION_IN_STATE)
		self._icon = config.get(CONF_ICON)

		_LOGGER.debug("ICS config: ")
		_LOGGER.debug("\tname: " + self._name)
		_LOGGER.debug("\tID: " + str(config.get(CONF_ID)))
		_LOGGER.debug("\turl: " + self._url)
		_LOGGER.debug("\tsw: " + self._sw)
		_LOGGER.debug("\ttimeformat: " + self._timeformat)
		_LOGGER.debug("\tlookahead: " + str(self._lookahead))
		_LOGGER.debug("\tshow_blank: " + str(self._show_blank))
		_LOGGER.debug("\tforce_update: " + str(self._force_update))
		_LOGGER.debug("\tshow_remaining: " + str(self._show_remaining))
		_LOGGER.debug("\tshow_ongoing: " + str(self._show_ongoing))
		_LOGGER.debug("\tgroup_events: " + str(self._group_events))
		_LOGGER.debug("\tn_skip: " + str(self._n_skip))
		_LOGGER.debug("\tdescription_in_state: " + str(self._description_in_state))
		_LOGGER.debug("\ticon: " + str(self._icon))

		self._lastUpdate = -1
		self.ics = {
			'extra': {
				'start': None,
				'end': None,
				'remaining': -999,
				'description': "-",
				'location': '-',
				'last_updated': None,
				'reload_at': None,
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
		return self._icon

	def fix_text(self, s):
		"""Remove Umlaute."""
		s = ''.join(e for e in s if (e.isalnum() or e == ' '))
		s = s.replace(chr(195), 'u')
		s = s.replace(chr(188), 'e')
		return s

	def exc(self):
		"""Print nicely formated exception."""
		_LOGGER.error("\n\n============= ICS Integration Error ================")
		_LOGGER.error("unfortunately ICS hit an error, please open a ticket at")
		_LOGGER.error("https://github.com/KoljaWindeler/ics/issues")
		_LOGGER.error("and paste the following output:\n")
		_LOGGER.error(traceback.format_exc())
		_LOGGER.error("\nthanks, Kolja")
		_LOGGER.error("============= ICS Integration Error ================\n\n")

	def check_fix_date_tz(self, event):
		"""Make sure all elements are timezone aware datetimes."""
		if(isinstance(event.dt, datetime.date) and not(isinstance(event.dt, datetime.datetime))):
			event.dt = datetime.datetime(event.dt.year, event.dt.month, event.dt.day)
		try:
			if(event.dt.tzinfo is None or event.dt.utcoffset() is None):
				event.dt = event.dt.replace(tzinfo=get_localzone())
		except Exception:
			pass
		return event

	def check_fix_rrule(self, calendar):
		"""Make sure that the UNITL date of the RRULE is the same type as DTSTART is.

		otherwise recurring_ical_events will crash.
		"""
		fix = 0
		for event in calendar.walk('vevent'):
			if("RRULE" in event):
				if("UNTIL" in event["RRULE"]):
					# different
					if(type(event["DTSTART"].dt) != type(event["RRULE"]["UNTIL"][0])):
						if(type(event["DTSTART"].dt) == datetime.datetime):
							d = event["RRULE"]["UNTIL"][0]
							event["RRULE"]["UNTIL"][0] = datetime.datetime(d.year, d.month, d.day)
						else:
							event["RRULE"]["UNTIL"][0] = event["RRULE"]["UNTIL"][0].date()
						fix += 1
					# tz fixing
					if(type(event["RRULE"]["UNTIL"][0]) == datetime.datetime):
						event["RRULE"]["UNTIL"][0] = event["RRULE"]["UNTIL"][0].replace(tzinfo=datetime.timezone.utc)
		return fix

	async def get_data(self):
		"""Update the actual data."""
		try:
			cal_string = await async_load_data(self.hass, self._url)
			cal = Calendar.from_ical(cal_string)

			# fix RRULE
			_LOGGER.debug(f"fixed {self.check_fix_rrule(cal)} RRule dates")

			# define calendar range
			start_date = datetime.datetime.now().replace(minute=0, hour=0, second=0, microsecond=0)
			end_date = start_date + datetime.timedelta(days=self._lookahead)

			# unfold calendar
			reoccuring_events = recurring_ical_events.of(cal).between(start_date, end_date)

			# make all item TZ aware datetime
			for event in reoccuring_events:
				if("DTSTART" in event):
					event["DTSTART"] = self.check_fix_date_tz(event["DTSTART"])
				if("DTEND" in event):
					event["DTEND"] = self.check_fix_date_tz(event["DTEND"])

			try:
				reoccuring_events = sorted(reoccuring_events, key=lambda x: x["DTSTART"].dt, reverse=False)
			except Exception:
				self.exc()

			self.ics['pickup_date'] = "no next event"
			self.ics['extra']['last_updated'] = datetime.datetime.now(get_localzone()).replace(microsecond=0)
			self.ics['extra']['reload_at'] = None
			self.ics['extra']['start'] = None
			self.ics['extra']['end'] = None
			self.ics['extra']['remaining'] = -999
			self.ics['extra']['description'] = "-"
			self.ics['extra']['location'] = "-"

			et = None
			skip_et = None
			n_skip = self._n_skip
			skip_reload_at = None
			event_date = None
			event_end_date = None

			# get now to check if events have started
			now = datetime.datetime.now(get_localzone())

			if(len(reoccuring_events) > 0):
				for e in reoccuring_events:
					# load start / end
					event_date = e["DTSTART"].dt
					if("DTEND" in e):
						event_end_date = e["DTEND"].dt
					else:
						event_end_date = event_date

					# handle empty or non existing summary field
					event_summary = self.fix_text(self._show_blank)
					if("SUMMARY" in e):
						if(self.fix_text(e["SUMMARY"]) != ""):
							event_summary = self.fix_text(e["SUMMARY"])

					if(event_summary):
						if(event_summary.lower().startswith(self.fix_text(self._sw).lower())):
							if((event_date > now) or (self._show_ongoing and event_end_date > now)):
								# logic to skip events, but save certain details,
								# e.g. reload / and timeslot for grouping
								if(n_skip > 0 or skip_et is not None):
									# note first  event_date as reload time
									if(skip_reload_at is None):
										skip_reload_at = event_date
									# if this event is the at the exact same time
									# as the last and we're grouping
									if(skip_et is not None and skip_et == event_date and self._group_events):
										# increase it temporary, will besically abolish the next line
										n_skip += 1
									n_skip -= 1
									skip_et = event_date
									if(n_skip >= 0):
										continue
									else:
										skip_et = None

								# if we hit this timeslot the firsttime, store everything
								if(et is None):
									self.ics['pickup_date'] = event_date.strftime(self._timeformat)
									self.ics['extra']['remaining'] = (event_date.date() - now.date()).days
									self.ics['extra']['description'] = event_summary
									self.ics['extra']['start'] = event_date.astimezone()
									self.ics['extra']['end'] = event_end_date.astimezone()
									if("LOCATION" in e):
										self.ics['extra']['location'] = self.fix_text(e["LOCATION"])
									et = event_date

								# if grouping is active and we hat it again, append
								elif((event_date == et) and (self._group_events)):
									self.ics['extra']['description'] += " / " + event_summary
									if("LOCATION" in e):
										self.ics['extra']['location'] += " / " + self.fix_text(e["LOCATION"])
									# store earliest end time
									if(self.ics['extra']['end'] > e["DTEND"].dt):
										self.ics['extra']['end'] = e["DTEND"].dt.astimezone()

								# this event hat a differnt timeslot then the first, so we don't append it and end here
								else:
									break

			# ----------- start of reload calucation -----------
			# base line for relaod is daybreak
			self.ics['extra']['reload_at'] = now.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)

			# check if the skip_reload at is easlier
			if(skip_reload_at is not None):
				if(skip_reload_at < self.ics['extra']['reload_at']):
					self.ics['extra']['reload_at'] = skip_reload_at

			# if we have a interval reload
			if(self._force_update > 0):
				force_reload_at = now + datetime.timedelta(seconds=self._force_update)
				if(force_reload_at < self.ics['extra']['reload_at']):
					self.ics['extra']['reload_at'] = force_reload_at

			# check if the next appointment is even earlier
			if(self._show_ongoing and event_end_date is not None):
					if(event_end_date < self.ics['extra']['reload_at']):
						self.ics['extra']['reload_at'] = event_end_date
			elif(event_date is not None):
					if(event_date < self.ics['extra']['reload_at']):
						self.ics['extra']['reload_at'] = event_date

			self.ics['extra']['reload_at'] = self.ics['extra']['reload_at'].replace(microsecond=0)
			# ----------- end of reload calucation -----------
		except Exception:
			self.ics['pickup_date'] = "failure"
			self.exc()


	async def async_update(self):
		"""Fetch new state data for the sensor.
		This is the only method that should fetch new data for Home Assistant.
		"""
		try:
			# first run
			if(self.ics['extra']['reload_at'] is None):
				await self.get_data()
			# check if we're past reload_at
			elif(self.ics['extra']['reload_at'] < datetime.datetime.now(get_localzone())):
				await self.get_data()

			# update states
			self._state_attributes = self.ics['extra']
			self._state = self.ics['pickup_date']
			if(self._show_remaining):
				self._state += ' (%02i)' % self.ics['extra']['remaining']
			if(self._description_in_state):
				self._state += ' ' + self.ics['extra']['description']
		except Exception:
			self._state = "error"
			self.exc()
