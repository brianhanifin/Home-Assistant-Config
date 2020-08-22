"""Config flow to configure Weatherbit component."""
import logging

from weatherbitpypi import Weatherbit, WeatherbitError

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import (
    CONF_API_KEY,
    CONF_ID,
    CONF_LATITUDE,
    CONF_LONGITUDE,
)
from homeassistant import config_entries, core
import homeassistant.helpers.config_validation as cv
from homeassistant.core import callback

from .const import (
    DOMAIN,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_FORECAST_LANGUAGE,
    CONF_ADD_SENSORS,
    CONF_ADD_ALERTS,
    CONF_CUR_UPDATE_INTERVAL,
    CONF_FCS_UPDATE_INTERVAL,
    CONF_FORECAST_LANGUAGE,
    CONF_WIND_UNITS,
    FORECAST_LANGUAGES,
    UNIT_WIND_MS,
    WIND_UNITS,
)

_LOGGER = logging.getLogger(__name__)


async def validate_input(hass: core.HomeAssistant, data):
    """Validate the user input allows us to connect.
    Data has the keys from DATA_SCHEMA with values provided by the user.
    """
    wbit_client = Weatherbit(
        data[CONF_API_KEY], data[CONF_LATITUDE], data[CONF_LONGITUDE],
    )

    unique_id = await wbit_client.async_get_city_name()

    return unique_id


class WeatherbitConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Weatherbit configuration flow."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return OptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        errors = {}

        if user_input is not None:
            await self.async_set_unique_id(
                f"{user_input[CONF_LATITUDE]}_{user_input[CONF_LONGITUDE]}"
            )
            self._abort_if_unique_id_configured()
            try:
                info = await validate_input(self.hass, user_input)
            except WeatherbitError:
                errors = {"base": "connection_error"}

            if "base" not in errors:
                return self.async_create_entry(
                    title=info,
                    data={
                        CONF_ID: info,
                        CONF_API_KEY: user_input[CONF_API_KEY],
                        CONF_LATITUDE: user_input[CONF_LATITUDE],
                        CONF_LONGITUDE: user_input.get(CONF_LONGITUDE),
                        CONF_WIND_UNITS: user_input.get(CONF_WIND_UNITS),
                        CONF_FORECAST_LANGUAGE: user_input.get(CONF_FORECAST_LANGUAGE),
                        CONF_FCS_UPDATE_INTERVAL: user_input.get(
                            CONF_FCS_UPDATE_INTERVAL
                        ),
                        CONF_CUR_UPDATE_INTERVAL: user_input.get(
                            CONF_CUR_UPDATE_INTERVAL
                        ),
                        CONF_ADD_SENSORS: user_input.get(CONF_ADD_SENSORS),
                        CONF_ADD_ALERTS: user_input.get(CONF_ADD_ALERTS),
                    },
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_API_KEY): str,
                    vol.Required(
                        CONF_LATITUDE, default=self.hass.config.latitude
                    ): cv.latitude,
                    vol.Required(
                        CONF_LONGITUDE, default=self.hass.config.longitude
                    ): cv.longitude,
                    vol.Optional(CONF_WIND_UNITS, default=UNIT_WIND_MS): vol.In(
                        WIND_UNITS
                    ),
                    vol.Optional(CONF_FORECAST_LANGUAGE, default="en"): vol.In(
                        FORECAST_LANGUAGES
                    ),
                    vol.Optional(
                        CONF_FCS_UPDATE_INTERVAL, default=DEFAULT_SCAN_INTERVAL
                    ): vol.All(vol.Coerce(int), vol.Range(min=30, max=120)),
                    vol.Optional(
                        CONF_CUR_UPDATE_INTERVAL, default=DEFAULT_SCAN_INTERVAL
                    ): vol.All(vol.Coerce(int), vol.Range(min=4, max=60)),
                    vol.Optional(CONF_ADD_SENSORS, default=True): bool,
                    vol.Optional(CONF_ADD_ALERTS, default=False): bool,
                }
            ),
            errors=errors,
        )


class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        CONF_WIND_UNITS,
                        default=self.config_entry.options.get(
                            CONF_WIND_UNITS, UNIT_WIND_MS
                        ),
                    ): vol.In(WIND_UNITS),
                    vol.Optional(
                        CONF_FORECAST_LANGUAGE,
                        default=self.config_entry.options.get(
                            CONF_FORECAST_LANGUAGE, DEFAULT_FORECAST_LANGUAGE
                        ),
                    ): vol.In(FORECAST_LANGUAGES),
                    vol.Optional(
                        CONF_FCS_UPDATE_INTERVAL,
                        default=self.config_entry.options.get(
                            CONF_FCS_UPDATE_INTERVAL, DEFAULT_SCAN_INTERVAL
                        ),
                    ): vol.All(vol.Coerce(int), vol.Range(min=30, max=120)),
                    vol.Optional(
                        CONF_CUR_UPDATE_INTERVAL,
                        default=self.config_entry.options.get(
                            CONF_CUR_UPDATE_INTERVAL, DEFAULT_SCAN_INTERVAL
                        ),
                    ): vol.All(vol.Coerce(int), vol.Range(min=4, max=60)),
                }
            ),
        )
