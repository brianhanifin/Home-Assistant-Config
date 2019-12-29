"""
This component provides support for HP Printers.
For more details about this component, please refer to the documentation at
https://home-assistant.io/components/hpprinter/
"""
import voluptuous as vol

from homeassistant.const import (CONF_HOST, CONF_NAME, CONF_DEVICES)
from homeassistant.helpers import config_validation as cv

from .const import *
from .HPDeviceData import *
from .home_assistant import HPPrinterHomeAssistant

_LOGGER = logging.getLogger(__name__)

DEVICE_SCHEMA = vol.Schema({
    vol.Required(CONF_HOST): cv.string,
    vol.Optional(CONF_NAME): cv.string
})

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_DEVICES, []): vol.All(cv.ensure_list, [vol.Any(DEVICE_SCHEMA)])
    }),
}, extra=vol.ALLOW_EXTRA)


def setup(hass, config):
    """Set up a Blue Iris component."""
    _LOGGER.debug(f"Loading HP Printer domain")

    initialized = False
    devices_handlers = []

    conf = config[DOMAIN]
    scan_interval = SCAN_INTERVAL
    devices = conf.get(CONF_DEVICES, [])

    device_id = 0

    for device in devices:
        try:
            device_id = device_id + 1

            host = device.get(CONF_HOST)
            name = device.get(CONF_NAME, f"{DEFAULT_NAME} #{device_id}")
            hp_data = None

            if host is not None:
                hp_data = HPDeviceData(host, name)

            ha = HPPrinterHomeAssistant(hass, scan_interval, name, hp_data)

            if host is not None:
                ha.initialize()

                devices_handlers.append(ha)

                _LOGGER.debug(f"{name} is loaded")
                initialized = True

            else:
                ha.notify_error_message(f"{name} was not configured correctly")

        except Exception as ex:
            exc_type, exc_obj, tb = sys.exc_info()
            line_number = tb.tb_lineno

            _LOGGER.error(f"Failed to create HA component, Error: {ex}, Line: {line_number}")

    hass.data[DATA_HP_PRINTER] = devices_handlers

    return initialized
