import logging

from homeassistant.core import callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.helpers.entity import Entity
from .const import *

_LOGGER = logging.getLogger(__name__)
DEPENDENCIES = [DOMAIN]


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the sensor platform."""
    ham_data = hass.data.get(DATA_HAM)

    if not ham_data:
        return

    sensors = []
    data_provider = {
            ATTR_WEEKDAY: {
                ATTR_STATE: ham_data.get_weekday,
                ATTR_ATTRIBUTES: None
            },
            ATTR_DAY_PART: {
                ATTR_STATE: ham_data.get_day_part,
                ATTR_ATTRIBUTES: None
            },
            ATTR_CURRENT_PROFILE: {
                ATTR_STATE: ham_data.get_current_profile,
                ATTR_ATTRIBUTES: ham_data.get_current_profile_data_parts
            },
            ATTR_CURRENT_SCENE: {
                ATTR_STATE: ham_data.get_current_scene,
                ATTR_ATTRIBUTES: None
            }
        }

    for sensor_type in SENSOR_TYPES:
        sensor_type_data = SENSOR_TYPES[sensor_type]
        sensor_name = sensor_type_data[0]
        sensor_icon = sensor_type_data[len(sensor_type_data) - 1]
        
        sensor = HomeAutomationManagerSensor(sensor_name, sensor_type, sensor_icon, hass, data_provider)
        
        sensors.append(sensor)
    
    add_entities(sensors, True)


class HomeAutomationManagerSensor(Entity):
    """Representation of a Sensor."""
    def __init__(self, sensor_name, sensor_type, sensor_icon, hass, data_provider):
        """Initialize the Home Profile sensor."""
        
        self._sensor_name = sensor_name
        self._sensor_type = sensor_type
        self._name = f'{DOMAIN.upper()} {self._sensor_name}'
        self._icon = f'mdi:{sensor_icon}'
        self._attributes = None
        self._data_provider_state = None
        self._data_provider_attributes = None
        
        sensor_id = f'{SENSOR_DOMAIN}.{self._name}'
        state_obj = hass.states.get(sensor_id)

        state = None
        if state_obj is not None:
            state = state_obj.state

        self._state = state
        
        current_data_provider = data_provider[self._sensor_type]
        
        if ATTR_STATE in current_data_provider:
            self._data_provider_state = current_data_provider[ATTR_STATE]
        
        if ATTR_ATTRIBUTES in current_data_provider:
            self._data_provider_attributes = current_data_provider[ATTR_ATTRIBUTES]
        
    @property
    def name(self):
        """Return the name of the device."""
        return self._name

    @property
    def friendly_name(self):
        """Return the name of the device."""
        return self._sensor_name

    @property
    def icon(self):
        return self._icon

    @property
    def device_class(self):
        """Return the class of this sensor."""
        return SENSOR_DEFAULT_DEVICE_CLASS

    @property
    def state(self):
        """Return the state of this sensor."""
        return self._state

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self._attributes
     
    async def async_added_to_hass(self):
        """Register callbacks."""
        async_dispatcher_connect(self.hass, SIGNAL_UPDATE_HAM, self._update_callback)

    @callback
    def _update_callback(self):
        """Call update method."""
        self.async_schedule_update_ha_state(True)

    def update(self):
        """Get the latest data."""
        if self._data_provider_state is not None:
            self._state = self._data_provider_state()
        
        if self._data_provider_attributes is not None:
            self._attributes = self._data_provider_attributes()
