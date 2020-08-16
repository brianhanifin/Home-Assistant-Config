import asyncio
import datetime
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import CONF_STYLE, CONF_STATION, CONF_LOOP, CONF_TYPE


_LOGGER = logging.getLogger(__name__)
PLATFORMS = ["camera"]
DEFAULT_SCAN_INTERVAL = datetime.timedelta(minutes=10)

def unique_id(config):
    name = f"{config[CONF_STATION]} {config[CONF_STYLE]} {config[CONF_TYPE]}"
    loop = config[CONF_LOOP]
    if isinstance(loop, bool):
        if loop:
            return f"{name} Loop"
        return name
    if loop > 1:
        return f"{name} Loop"
    return name

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up nwsradar integration."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up a National Weather Service entry."""
    for component in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, component)
        )
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, component)
                for component in PLATFORMS
            ]
        )
    )
    return unload_ok
