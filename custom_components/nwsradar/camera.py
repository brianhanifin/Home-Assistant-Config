"""Provide animated GIF loops of NWS radar imagery."""
from datetime import timedelta
import logging
import voluptuous as vol

from homeassistant.components.camera import PLATFORM_SCHEMA, Camera
from homeassistant.const import CONF_NAME
from homeassistant.helpers import config_validation as cv
from homeassistant.util import Throttle

_LOGGER = logging.getLogger(__name__)

CONF_FRAMES = 'frames'
CONF_STATION = 'station'
CONF_TYPE = 'type'

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=5)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_STATION): cv.string,
    vol.Optional(CONF_FRAMES): cv.positive_int,
    vol.Optional(CONF_NAME): cv.string,
    vol.Optional(CONF_TYPE): cv.string,
})

RADARTYPES = ['NCR', 'N0R', 'N0S', 'N1P', 'NTP', 'N0Z']


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up NWS radar-loop camera component."""
    station = config[CONF_STATION]
    name = config.get(CONF_NAME) or config[CONF_STATION]
    frames = config.get(CONF_FRAMES) or 6
    radartype = config.get(CONF_TYPE) or 'NCR'
    if radartype not in RADARTYPES:
        _LOGGER.error('invalid radar type')
    add_entities([NWSRadarCam(name, radartype.upper(), station.upper(), frames)])


class NWSRadarCam(Camera):
    """A camera component producing animated NWS radar GIFs."""

    def __init__(self, name, radartype, station, frames):
        """Initialize the component."""
        from nws_radar import Nws_Radar
        super().__init__()
        self._name = name
        self._cam = Nws_Radar(station, radartype, nframes=frames)
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

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        _LOGGER.debug("update image")
        self._cam.update()
        self._image = self._cam.image()
