"""
This component provides support for Home Automation Manager (HAM).
For more details about this component, please refer to the documentation at
https://home-assistant.io/components/ham/
"""
import logging


from homeassistant.components.switch import DOMAIN as SWITCH_DOMAIN
from homeassistant.components.input_boolean import DOMAIN as INPUT_BOOLEAN_DOMAIN

from .const import VERSION
from .const import *
from .configuration_transformer import HomeAutomationManagerConfigurationTransformer
from .ham_data import HomeAutomationManagerData

_LOGGER = logging.getLogger(__name__)

DEPENDENCIES = [DEVICE_TRACKER_DOMAIN, INPUT_BOOLEAN_DOMAIN, SWITCH_DOMAIN]


def setup(hass, config):
    """Set up an Home Automation Manager component."""

    try:
        conf = config[DOMAIN]
        scan_interval = SCAN_INTERVAL
        default_profile = conf.get(CONF_PROFILE_DEFAULT)
        profiles = conf.get(CONF_PROFILES)
        events = conf.get(CONF_EVENTS)
        trackers = conf.get(CONF_TRACKERS)
        scenes = conf.get(CONF_SCENES)
        default_profile_parts = default_profile[CONF_PARTS]

        ham_configuration_transformer = HomeAutomationManagerConfigurationTransformer(default_profile_parts, profiles,
                                                                                      events, trackers, scenes)
        configuration = ham_configuration_transformer.get_configuration()

        data = HomeAutomationManagerData(hass, scan_interval, configuration)

        was_initialized = data.was_initialized()

        if was_initialized:
            hass.data[DATA_HAM] = data

        return was_initialized

    except Exception as ex:
        _LOGGER.error('Error while initializing HAM, exception: {}'.format(str(ex)))

        hass.components.persistent_notification.create(
            f'Error: {str(ex)}<br />You will need to restart hass after fixing.',
            title=NOTIFICATION_TITLE,
            notification_id=NOTIFICATION_ID)

        return False
