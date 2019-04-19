"""
Use serial protocol of EMU2 meter to obtain state of the connected meter.
For more details about this component, please refer to the documentation
at https://github.com/jrhorrisberger/home-assistant/custom_components/rainforest
"""

from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_NAME, EVENT_HOMEASSISTANT_STOP)
import logging
import voluptuous as vol
from threading import Thread

__version__ = '0.2.0'

_LOGGER = logging.getLogger(__name__)

DOMAIN = "rainforest"

DEFAULT_NAME = "Rainforest Energy Monitoring Unit"
CONF_PORT = 'port'

ATTR_DEVICE_MAC_ID = "Device MAC ID"
ATTR_METER_MAC_ID = "Meter MAC ID"
ATTR_TEIR = "Price Teir"
ATTR_PRICE = "Price"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_PORT): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    _LOGGER.debug("Loading")
    port = config.get(CONF_PORT)
    sensor_name = config.get(CONF_NAME)

    sensor = EMU2Sensor(sensor_name, port)

    hass.bus.async_listen_once(
        EVENT_HOMEASSISTANT_STOP, sensor.stop_serial_read())

    async_add_entities([sensor])

class EMU2Sensor(Entity):
    def __init__(self, sensor_name, port):
        _LOGGER.debug("Init")
        self._port = port
        self._name = sensor_name
        self._baudrate = 115200
        self._timeout = 1
        self._icon = 'mdi:flash'
        self._unit_of_measurement = "kWh"
        
        self._serial_thread = None
        self._serial_thread_isEnabled = True

        self._state = None

        self._data = {}                
        self._data[ATTR_DEVICE_MAC_ID] = None
        self._data[ATTR_METER_MAC_ID] = None
        self._data[ATTR_TEIR] = None
        self._data[ATTR_PRICE] = None

    @property
    def name(self):
        return self._name

    @property
    def device_state_attributes(self):
        return {
            ATTR_DEVICE_MAC_ID: self._data.get(ATTR_DEVICE_MAC_ID),
            ATTR_METER_MAC_ID: self._data.get(ATTR_METER_MAC_ID),
            ATTR_TEIR: self._data.get(ATTR_TEIR),
            ATTR_PRICE: self._data.get(ATTR_PRICE),
        }
        
    @property
    def icon(self):
        return self._icon

    @property
    def state(self):
        return self._state

    @property
    def should_poll(self):
        return False

    @property
    def unit_of_measurement(self):
        return self._unit_of_measurement

    async def async_added_to_hass(self):
        _LOGGER.debug("Thread Start")
        self._serial_thread = Thread(target = self.serial_read, args = (self._port, self._baudrate, self._timeout))
        self._serial_thread.start()

    def serial_read(self, portIN, baudrateIN, timeoutIN, **kwargs):
        
        _LOGGER.debug("Thread Starting")
        import serial, time
        import xml.etree.ElementTree as xmlDecoder

        reader = None
        while reader == None:
            try:
                reader = serial.Serial(portIN, baudrateIN, timeout=timeoutIN)
            except:
                _LOGGER.error("Failed to open %s. Retrying in 5s...", portIN)
                time.sleep(5.0)

        
        _LOGGER.debug("Begining Loop")
        while self._serial_thread_isEnabled:
            if (reader.in_waiting > 0):
                #_LOGGER.debug("Data RX")
                msgStr = reader.read(reader.in_waiting).decode()

                if msgStr != [] and msgStr[0] == '<':
                    try:
                        xmlTree = xmlDecoder.fromstring(msgStr)
                    except:
                        continue
                                
                    if xmlTree.tag == 'InstantaneousDemand':
                        demand = int(xmlTree.find('Demand').text, 16)
                        multiplier = int(xmlTree.find('Multiplier').text, 16)
                        divisor = int(xmlTree.find('Divisor').text, 16)
                        digitsRight = int(xmlTree.find('DigitsRight').text, 16)

                        if(divisor != 0):
                            self._state = round(((demand * multiplier) / divisor), digitsRight)

                        self._data[ATTR_DEVICE_MAC_ID] = xmlTree.find('DeviceMacId').text
                        self._data[ATTR_METER_MAC_ID] = xmlTree.find('MeterMacId').text

                        self.async_schedule_update_ha_state()
                        
                        _LOGGER.debug("InstantaneousDemand: %s", self._state)

                    elif xmlTree.tag == 'PriceCluster':
                        priceRaw = int(xmlTree.find('Price').text, 16)
                        trailingDigits = int(xmlTree.find('TrailingDigits').text, 16)
                        self._data[ATTR_PRICE] = priceRaw / pow(10, trailingDigits)

                        self._data[ATTR_TEIR] = int(xmlTree.find('Tier').text, 16)
                        
                        _LOGGER.debug("PriceCluster: %s", self._data[ATTR_PRICE])
            else:
                time.sleep(0.5)

        reader.close()

    async def stop_serial_read(self):
        self._serial_thread_isEnabled = False