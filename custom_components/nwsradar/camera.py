"""Provide animated GIF loops of NWS radar imagery."""
from datetime import timedelta
import logging
import voluptuous as vol

from nws_radar.nws_radar_mosaic import REGIONS

from homeassistant.components.camera import Camera, PLATFORM_SCHEMA
from homeassistant.config_entries import SOURCE_IMPORT
from homeassistant.helpers import config_validation as cv

from . import unique_id
from .const import (
    CONF_STATION,
    CONF_TYPE,
    CONF_LOOP,
    CONF_STYLE,
    RADAR_TYPES,
    CONF_NAME,
    STYLES,
    DOMAIN,
    DATA_COORDINATOR,
    DATA_CAM,
)

_LOGGER = logging.getLogger(__name__)

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=5)

CONF_FRAMES = "frames"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_STATION): cv.string,
        vol.Optional(CONF_STYLE, default="Standard"): vol.In(STYLES),
        vol.Optional(CONF_FRAMES): cv.positive_int,
        vol.Optional(CONF_NAME): cv.string,
        vol.Optional(CONF_TYPE, default="NCR"): vol.In(RADAR_TYPES.values()),
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up NWS radar-loop camera component."""
    _LOGGER.warning(
        "YAML configuration deprecated. It will be removed in nwsradar v0.6.0"
    )
    station = config[CONF_STATION].upper()
    style = config.get(CONF_STYLE) or "Standard"
    name = config.get(CONF_NAME) or config[CONF_STATION]
    frames = config.get(CONF_FRAMES) or 6
    loop = frames > 1

    radartype = config.get(CONF_TYPE) or "NCR"
    if radartype not in RADAR_TYPES.values():
        _LOGGER.error("invalid radar type")
    radartype = next(iter([k for k, v in RADAR_TYPES.items() if v == radartype]))

    if style == "Mosaic":
        if station not in REGIONS:
            _LOGGER.error("station {station} not in %s", REGIONS)

    entry_data = {
        CONF_STATION: station,
        CONF_STYLE: style,
        CONF_LOOP: loop,
        CONF_TYPE: radartype,
        CONF_NAME: name,
    }

    hass.async_create_task(
        hass.config_entries.flow.async_init(
            DOMAIN, context={"source": SOURCE_IMPORT}, data=entry_data
        )
    )


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the nwsradar camera platform."""
    name = entry.data.get(CONF_NAME, unique_id(entry.data))

    coordinator = hass.data[DOMAIN][entry.entry_id][DATA_COORDINATOR]
    cam = hass.data[DOMAIN][entry.entry_id][DATA_CAM]
    async_add_entities([NWSRadarCam(unique_id(entry.data), name, coordinator, cam)])


class NWSRadarCam(Camera):
    """A camera component producing animated NWS radar GIFs."""

    def __init__(self, id_unique, name, coordinator, cam):
        """Initialize the component."""
        super().__init__()
        self._name = name
        self._unique_id = id_unique
        self._cam = cam
        self._coordinator = coordinator

    @property
    def should_poll(self):
        return False

    def camera_image(self):
        """Return the current NWS radar loop"""
        _LOGGER.debug("display image")
        return self._cam.image()

    @property
    def name(self):
        """Return the component name."""
        return self._name

    @property
    def unique_id(self):
        """Return unique_id."""
        return self._unique_id

    @property
    def available(self):
        """Return availabilty of data."""
        return self._coordinator.last_update_success

    async def async_update(self):
        """Manual update entity."""
        await self._coordinator.async_request_refresh()

    async def async_added_to_hass(self):
        """When entity is added to hass."""
        self.async_on_remove(
            self._coordinator.async_add_listener(self.async_write_ha_state)
        )
