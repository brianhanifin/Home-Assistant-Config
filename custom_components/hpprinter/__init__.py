"""
This component provides support for HP Printers.
For more details about this component, please refer to the documentation at
https://home-assistant.io/components/hpprinter/
"""
from homeassistant.config_entries import ConfigEntry

from homeassistant.const import (CONF_HOST, CONF_NAME)
from homeassistant.core import HomeAssistant

from .const import *
from .HPDeviceData import *
from .home_assistant import HPPrinterHomeAssistant

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass, config):
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up a HPPrinter component."""
    _LOGGER.debug(f"Loading HP Printer domain")

    _LOGGER.debug(f"Starting async_setup_entry of {DOMAIN}")
    entry_data = entry.data

    host = entry_data.get(CONF_HOST)
    data = {}

    if DATA_HP_PRINTER not in hass.data:
        hass.data[DATA_HP_PRINTER] = data

    name = entry_data.get(CONF_NAME, f"{DEFAULT_NAME} #{len(data) + 1}")

    if host is None:
        _LOGGER.info("Invalid hostname")
        return False

    if name in data:
        _LOGGER.info(f"Printer {name} already defined")
        return False

    hp_data = HPDeviceData(host, name)

    ha = HPPrinterHomeAssistant(hass, SCAN_INTERVAL, name, hp_data)
    ha.initialize()

    hass.data[DATA_HP_PRINTER][name] = ha

    return True
