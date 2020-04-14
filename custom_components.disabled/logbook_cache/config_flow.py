"""Config flow for Logbook Cache integration."""
import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import config_entry_flow
import homeassistant.helpers.config_validation as cv

from .const import (
    DOMAIN,
    NAME,
    CACHE_DAYS,
    ONLY_CACHE,
    DEFAULT_CACHE_DAYS,
    DEFAULT_ONLY_CACHE,
)

_LOGGER = logging.getLogger(__name__)


class LogbookCacheFlowHandler(config_entry_flow.DiscoveryFlowHandler):
    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return OptionsFlowHandler(config_entry)


class OptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CACHE_DAYS,
                        default=self.config_entry.options.get(
                            CACHE_DAYS, DEFAULT_CACHE_DAYS
                        ),
                    ): vol.All(vol.Coerce(int), vol.Range(min=1)),
                    vol.Required(
                        ONLY_CACHE,
                        default=self.config_entry.options.get(
                            ONLY_CACHE, DEFAULT_ONLY_CACHE
                        ),
                    ): bool,
                }
            ),
        )


class DiscoveryFlow(LogbookCacheFlowHandler):
    def __init__(self):
        super().__init__(
            DOMAIN, NAME, lambda hass: True, config_entries.CONN_CLASS_UNKNOWN
        )


config_entries.HANDLERS.register(DOMAIN)(DiscoveryFlow)
