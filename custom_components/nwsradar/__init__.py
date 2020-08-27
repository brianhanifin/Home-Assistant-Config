"""National Weather Service Radar integration."""
import asyncio
import datetime
import logging

import async_timeout
from nws_radar import Nws_Radar, Nws_Radar_Lite, Nws_Radar_Mosaic

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import (
    CONF_STYLE,
    CONF_STATION,
    CONF_LOOP,
    CONF_TYPE,
    DOMAIN,
    DATA_COORDINATOR,
    DATA_CAM,
    RADAR_TYPES,
)


_LOGGER = logging.getLogger(__name__)
PLATFORMS = ["camera"]
SCAN_INTERVAL = datetime.timedelta(minutes=10)


def unique_id(config):
    """Return unique_id from config."""
    name = f"{config[CONF_STATION]} {config[CONF_STYLE]} {config[CONF_TYPE]}"
    loop = config[CONF_LOOP]
    if loop:
        return f"{name} Loop"
    return name


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up nwsradar integration."""
    hass.data[DOMAIN] = dict()
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up a National Weather Service entry."""
    hass_data = hass.data.setdefault(DOMAIN, {})

    station = entry.data[CONF_STATION]
    style = entry.data[CONF_STYLE]
    loop = entry.data[CONF_LOOP]

    frames = 6 if loop else 1

    if style == "Enhanced":
        radartype = RADAR_TYPES[entry.data[CONF_TYPE]]
        cam = Nws_Radar(station, radartype, nframes=frames)
    elif style == "Standard":
        radartype = RADAR_TYPES[entry.data[CONF_TYPE]]
        cam = Nws_Radar_Lite(station, radartype, loop)
    elif style == "Mosaic":
        cam = Nws_Radar_Mosaic(station, nframes=frames)

    async def async_update_cam():
        _LOGGER.debug("updating camera")
        async with async_timeout.timeout(10):
            return await hass.async_add_executor_job(cam.update)

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=unique_id(entry.data),
        update_method=async_update_cam,
        update_interval=SCAN_INTERVAL,
    )

    hass_data[entry.entry_id] = {DATA_COORDINATOR: coordinator, DATA_CAM: cam}

    await coordinator.async_refresh()

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
