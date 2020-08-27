"""Config flow for National Weather Service (NWS) integration."""
import logging

import voluptuous as vol
from nws_radar.nws_radar_mosaic import REGIONS

from homeassistant import config_entries

from . import unique_id

# pylint: disable=unused-import
from .const import (
    CONF_LOOP,
    CONF_STATION,
    CONF_STYLE,
    STYLES,
    CONF_TYPE,
    RADAR_TYPES,
    DEFAULT_RADAR_TYPE,
    CONF_NAME,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for National Weather Service (NWS)."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            self._config = user_input  # pylint: disable=attribute-defined-outside-init
            if user_input[CONF_STYLE] in {"Standard", "Enhanced"}:
                return await self.async_step_standard_enhanced()
            # Mosaic
            return await self.async_step_mosaic()
        data_schema = vol.Schema({vol.Required(CONF_STYLE): vol.In(STYLES),})
        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )

    async def async_step_standard_enhanced(self, user_input=None):
        """Standard or enhanced step."""
        errors = {}
        if user_input is not None:
            self._config.update(user_input)
            self._config[CONF_STATION] = self._config[CONF_STATION].upper()
            title = unique_id(self._config)
            self._config[CONF_NAME] = None

            await self.async_set_unique_id(unique_id(self._config))
            self._abort_if_unique_id_configured()

            return self.async_create_entry(title=title, data=self._config)
        data_schema = vol.Schema(
            {
                vol.Required(CONF_STATION): str,
                vol.Required(CONF_LOOP, default=True): bool,
                vol.Required(CONF_TYPE, default=DEFAULT_RADAR_TYPE): vol.In(
                    RADAR_TYPES.keys()
                ),
            }
        )
        return self.async_show_form(
            step_id="standard_enhanced", data_schema=data_schema, errors=errors
        )

    async def async_step_mosaic(self, user_input=None):
        """Mosaic step."""
        errors = {}
        if user_input is not None:
            self._config.update(user_input)
            self._config[CONF_TYPE] = ""
            self._config[CONF_NAME] = None
            title = unique_id(self._config)
            await self.async_set_unique_id(title)
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title=title, data=self._config)
        data_schema = vol.Schema(
            {
                vol.Required(CONF_STATION): vol.In(REGIONS),
                vol.Required(CONF_LOOP, default=True): bool,
            }
        )
        return self.async_show_form(
            step_id="mosaic", data_schema=data_schema, errors=errors
        )

    async def async_step_import(self, user_input=None):
        """Import an entry from yaml."""
        title = unique_id(user_input)
        await self.async_set_unique_id(title)
        self._abort_if_unique_id_configured()

        return self.async_create_entry(title=title, data=user_input)
