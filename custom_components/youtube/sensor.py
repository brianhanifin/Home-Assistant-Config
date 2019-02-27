"""
A platform which give you info about the newest video on a channel.

For more details about this component, please refer to the documentation at
https://github.com/custom-components/sensor.youtube
"""

import html
import logging
import requests
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.entity import Entity

__version__ = '0.0.3'

CONF_CHANNEL_ID = 'channel_id'

ICON = 'mdi:youtube'

BASE_URL = 'https://www.youtube.com/feeds/videos.xml?channel_id={}'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_CHANNEL_ID): cv.string,
})

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(
        hass, config, async_add_entities, discovery_info=None):
    channel_id = config['channel_id']
    try:
        url = BASE_URL.format(channel_id)
        info = requests.get(url).text
        name = html.parser.HTMLParser().unescape(
            info.split('<title>')[1].split('</')[0])
    except Exception:
        name = None

    if name is not None:
        async_add_entities([YoutubeSensor(channel_id, name)], True)

class YoutubeSensor(Entity):
    def __init__(self, channel_id, name):
        self._state = None
        self._image = None
        self._name = name
        self.channel_id = channel_id
        self.attr = {}

    async def async_update(self):
        try:
            url = BASE_URL.format(self.channel_id)
            info = requests.get(url).text
            title = html.parser.HTMLParser().unescape(
                info.split('<title>')[2].split('</')[0])
            url = info.split('<link rel="alternate" href="')[2].split('"/>')[0]
            published = info.split('<published>')[2].split('</')[0]
            thumbnail_url = info.split(
                '<media:thumbnail url="')[1].split('"')[0]
            self._state = title
            self._image = thumbnail_url
            self.attr = {'url': url, 'published': published}
        except:
            _LOGGER.debug('Could not update')

    @property
    def name(self):
        return self._name

    @property
    def entity_picture(self):
        return self._image

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return ICON

    @property
    def device_state_attributes(self):
        return self.attr
