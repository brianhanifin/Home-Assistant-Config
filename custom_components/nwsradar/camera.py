"""Provide animated GIF loops of NWS radar imagery."""
from datetime import timedelta
import logging
import voluptuous as vol

from nws_radar import Nws_Radar, Nws_Radar_Lite, Nws_Radar_Mosaic
from nws_radar.nws_radar_mosaic import REGIONS

from homeassistant.components.camera import Camera, PLATFORM_SCHEMA
from homeassistant.config_entries import SOURCE_IMPORT
from homeassistant.helpers import config_validation as cv
from homeassistant.util import Throttle

from . import unique_id
from .const import CONF_STATION, CONF_TYPE, CONF_LOOP, CONF_STYLE, RADAR_TYPES, CONF_NAME, STYLES, DOMAIN

_LOGGER = logging.getLogger(__name__)

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=5)

CONF_FRAMES = "frames"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_STATION): cv.string,
    vol.Optional(CONF_STYLE, default='Standard'): vol.In(STYLES),
    vol.Optional(CONF_FRAMES): cv.positive_int,
    vol.Optional(CONF_NAME): cv.string,
    vol.Optional(CONF_TYPE, default='NCR'): vol.In(RADAR_TYPES.values()),
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up NWS radar-loop camera component."""
    _LOGGER.warning("YAML configuration deprecated. It will be removed in nwsradar v0.6.0")
    station= config[CONF_STATION].upper()
    style = config.get(CONF_STYLE) or 'Standard'
    name = config.get(CONF_NAME) or config[CONF_STATION]
    frames = config.get(CONF_FRAMES) or 6
    loop = True if frames > 1 else False

    radartype = config.get(CONF_TYPE) or 'NCR'
    if radartype not in RADAR_TYPES.values():
        _LOGGER.error('invalid radar type')
    radartype = next(iter([k for k, v in RADAR_TYPES.items() if v==radartype]))

    if style == 'Mosaic':
        if station not in REGIONS:
            _LOGGER.error(f"station {station} not 8in {REGIONS}")

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
    station = entry.data[CONF_STATION]
    style = entry.data[CONF_STYLE]
    frames = 6 if entry.data[CONF_LOOP] else 1
    if entry.data[CONF_TYPE]:
        radartype = RADAR_TYPES[entry.data[CONF_TYPE]]
    else:
        radartype = ""
    name = entry.data.get(CONF_NAME, unique_id(entry.data))
    async_add_entities([NWSRadarCam(unique_id(entry.data), radartype.upper(), station.upper(), frames, style, name)])


class NWSRadarCam(Camera):
    """A camera component producing animated NWS radar GIFs."""

    def __init__(self, unique_id, radartype, station, frames, style, name):
        """Initialize the component."""
        super().__init__()
        self._name = name
        self._unique_id = unique_id
        if style == 'Enhanced':
            self._cam = Nws_Radar(station, radartype, nframes=frames)
        elif style == 'Standard':
            if frames == 1:
                self._cam = Nws_Radar_Lite(station, radartype, loop=False)
            else:
                self._cam = Nws_Radar_Lite(station, radartype, loop=True)
        elif style == 'Mosaic':
            self._cam = Nws_Radar_Mosaic(station, nframes=frames)  
        self._image = None

    @property
    def should_poll(self):
        return True
    
    def camera_image(self):
        """Return the current NWS radar loop"""
        self.update()
        _LOGGER.debug("display image")
        return self._image

    @property
    def name(self):
        """Return the component name."""
        return self._name

    @property
    def unique_id(self):
        """Return unique_id."""
        return self._unique_id
    
    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        _LOGGER.debug("update image")
        self._cam.update()
        self._image = self._cam.image()
