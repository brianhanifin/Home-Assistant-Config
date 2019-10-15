import asyncio

import logging

from homeassistant.core import callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.const import (STATE_ON)
from homeassistant.components.binary_sensor import (BinarySensorDevice)
from homeassistant.components.binary_sensor import DOMAIN as BINARY_SENSOR_DOMAIN
from .const import *

_LOGGER = logging.getLogger(__name__)

DEPENDENCIES = [DOMAIN]


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the sensor platform."""
    ham_data = hass.data.get(DATA_HAM)
    if not ham_data:
        return

    sensors = []

    all_profiles = ham_data.get_profiles()

    _LOGGER.debug('Loading HAM Binary Sensors')

    for profile_name in all_profiles:
        sensor_name = f'Profile {profile_name}'
        attributes = ham_data.get_profile_data(profile_name)

        _LOGGER.debug(f'{sensor_name} - data: {attributes}')

        sensor = HomeAutomationManagerBinarySensor(sensor_name, attributes, ham_data, hass)

        sensors.append(sensor)

    add_entities(sensors, True)


class HomeAutomationManagerBinarySensor(BinarySensorDevice):
    """Representation of a Sensor."""

    def __init__(self, sensor_name, attributes, ham_data, hass):
        """Initialize the Home Profile sensor."""

        self._sensor_name = sensor_name
        self._name = f'{DOMAIN.upper()} {self._sensor_name}'
        self._attributes = attributes
        self._ham_data = ham_data

        binary_sensor_id = f'{BINARY_SENSOR_DOMAIN}.{self._name}'
        state_obj = hass.states.get(binary_sensor_id)

        self._is_on = state_obj is not None and state_obj.state == STATE_ON

    @property
    def name(self):
        """Return the name of the device."""
        return self._name

    @property
    def friendly_name(self):
        """Return the name of the device."""
        return self._sensor_name

    @property
    def device_class(self):
        """Return the class of this sensor."""
        return BINARY_SENSOR_DEFAULT_DEVICE_CLASS

    @property
    def icon(self):
        return 'mdi:{}'.format(BINARY_SENSOR_DEFAULT_ICON)

    @property
    def is_on(self):
        """Return true if the binary sensor is on."""
        return self._is_on

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self._attributes

    @asyncio.coroutine
    def async_added_to_hass(self):
        """Register callbacks."""
        async_dispatcher_connect(self.hass, SIGNAL_UPDATE_HAM, self._update_callback)

    @callback
    def _update_callback(self):
        """Call update method."""
        self.async_schedule_update_ha_state(True)

    def update(self):
        """Get the latest data."""
        is_on = False

        if self._ham_data is not None:
            current_profile = self._ham_data.get_current_profile()
            is_away = self._ham_data.get_is_away()
            sensor_name = self._sensor_name.replace("Profile ", "")

            if current_profile is not None and is_away is not None:
                if sensor_name == current_profile:
                    _LOGGER.debug(f'{current_profile} equals {sensor_name}')
                    is_on = True

                elif sensor_name == DEFAULT_PROFILE:
                    _LOGGER.debug('Default is active')
                    is_on = True

                elif sensor_name == AWAY_PROFILE and is_away:
                    _LOGGER.debug('Away is active')
                    is_on = True

                else:
                    _LOGGER.debug('{sensor_name} is inactive')

                self._is_on = is_on
