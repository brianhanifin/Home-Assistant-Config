"""Support for the Weatherbit weather service."""
import asyncio
from datetime import timedelta
import logging
from typing import Dict, List

import aiohttp
import async_timeout
from weatherbitpypi import Weatherbit, WeatherbitError

from homeassistant.components.weather import (
    ATTR_FORECAST_CONDITION,
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_TEMP,
    ATTR_FORECAST_TEMP_LOW,
    ATTR_FORECAST_TIME,
    ATTR_FORECAST_WIND_BEARING,
    ATTR_FORECAST_WIND_SPEED,
    WeatherEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_LATITUDE,
    CONF_LONGITUDE,
    CONF_ID,
    CONF_API_KEY,
    EVENT_CORE_CONFIG_UPDATE,
    LENGTH_METERS,
    LENGTH_MILES,
    LENGTH_KILOMETERS,
    PRESSURE_HPA,
    PRESSURE_INHG,
    TEMP_CELSIUS,
)
from homeassistant.helpers.typing import HomeAssistantType
from homeassistant.helpers import aiohttp_client
from homeassistant.util import Throttle, slugify
from homeassistant.util.distance import convert as convert_distance
from homeassistant.util.pressure import convert as convert_pressure
import homeassistant.helpers.device_registry as dr

from .const import (
    ATTR_WEATHERBIT_AQI,
    ATTR_WEATHERBIT_CLOUDINESS,
    ATTR_WEATHERBIT_IS_NIGHT,
    ATTR_WEATHERBIT_WIND_GUST,
    ATTR_WEATHERBIT_PRECIPITATION,
    ATTR_WEATHERBIT_UVI,
    ENTITY_ID_SENSOR_FORMAT,
    DEFAULT_ATTRIBUTION,
)

_LOGGER = logging.getLogger(__name__)

# Used to map condition from API results
CONDITION_CLASSES = {
    "clear-night": [8000],
    "cloudy": [803, 804],
    "exceptional": [],
    "fog": [741],
    "hail": [623],
    "lightning": [230, 231],
    "lightning-rainy": [200, 201, 202],
    "partlycloudy": [801, 802],
    "pouring": [502, 522],
    "rainy": [300, 301, 302, 500, 501, 511, 520, 521],
    "snowy": [600, 601, 602, 621, 622, 623],
    "snowy-rainy": [610, 611, 612],
    "sunny": [800],
    "windy": [],
    "windy-variant": [],
}

# 5 minutes between retrying connect to API again
RETRY_TIMEOUT = 5 * 60

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=30)


async def async_setup_entry(
    hass: HomeAssistantType, entry: ConfigEntry, async_add_entities
) -> None:
    """Add a weather entity from map location."""

    session = aiohttp_client.async_get_clientsession(hass)

    entity = WeatherbitWeather(
        entry.data[CONF_ID],
        entry.data[CONF_API_KEY],
        entry.data[CONF_LATITUDE],
        entry.data[CONF_LONGITUDE],
        hass.config.units.is_metric,
        session,
    )

    async_add_entities([entity], True)

    return True


class WeatherbitWeather(WeatherEntity):
    """Representation of a weather entity."""

    def __init__(
        self,
        name: str,
        api_key: str,
        latitude: str,
        longitude: str,
        is_metric: bool,
        session: aiohttp.ClientSession = None,
    ) -> None:
        """Initialize the Weatherbit weather entity."""

        self._name = name.capitalize()
        self._api_key = api_key
        self._latitude = latitude
        self._longitude = longitude
        self._is_metric = is_metric
        self._forecasts = None
        self._current = None
        self._fail_count = 0
        self._api = Weatherbit(
            self._api_key, self._latitude, self._longitude, "en", "M", session=session
        )

    @property
    def unique_id(self) -> str:
        """Return a unique id."""
        return f"{self._latitude}, {self._longitude}"

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    async def async_update(self) -> None:
        """Refresh the forecast data from Weatherbit weather API."""
        try:
            with async_timeout.timeout(10):
                self._forecasts = await self.get_weather_forecast()
                self._current = await self.get_weather_current()
                self._fail_count = 0
                _LOGGER.debug("WEATHERBIT: FORECAST UPDATED")

        except (asyncio.TimeoutError, WeatherbitError):
            _LOGGER.error("Failed to connect to Weatherbit API, retry in 5 minutes")
            self._fail_count += 1
            if self._fail_count < 3:
                self.hass.helpers.event.async_call_later(
                    RETRY_TIMEOUT, self.retry_update
                )

    async def retry_update(self, _):
        """Retry refresh weather forecast."""
        await self.async_update()

    async def get_weather_forecast(self) -> []:
        """Return the current forecasts from Weatherbit API."""
        return await self._api.async_get_forecast_daily()

    async def get_weather_current(self) -> []:
        """Return the current weather from Weatherbit API."""
        return await self._api.async_get_current_data()

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return self._name

    @property
    def temperature(self) -> int:
        """Return the temperature."""
        if self._current is not None:
            return self._current[0].temp
        return None

    @property
    def temperature_unit(self) -> str:
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    @property
    def humidity(self) -> int:
        """Return the humidity."""
        if self._current is not None:
            return self._current[0].humidity
        return None

    @property
    def wind_speed(self) -> float:
        """Return the wind speed."""
        speed_m_s = self._current[0].wind_spd
        if self._is_metric or speed_m_s is None:
            return round(float(speed_m_s) * 3.6, 1)

        return round(float(speed_m_s * 2.23693629), 2)

    @property
    def wind_gust(self) -> float:
        """Return the wind Gust."""
        speed_m_s = self._forecasts[0].wind_gust_spd
        if self._is_metric or speed_m_s is None:
            return round(speed_m_s, 1)

        return round(float(speed_m_s * 2.23693629), 2)

    @property
    def wind_bearing(self) -> int:
        """Return the wind bearing."""
        if self._current is not None:
            return self._current[0].wind_dir
        return None

    @property
    def precipitation(self) -> float:
        """Return the precipitation."""
        if self._is_metric or self._current[0].precip is None:
            return round(float(self._current[0].precip), 1)

        return round(float(self._current[0].precip) / 25.4, 2)

    @property
    def ozone(self) -> float:
        """Return the ozone."""
        if self._forecasts is not None:
            return self._forecasts[0].ozone
        return None

    @property
    def visibility(self) -> float:
        """Return the visibility."""
        visibility_km = self._current[0].vis
        if self._is_metric or visibility_km is None:
            return visibility_km

        visibility_mi = convert_distance(visibility_km, LENGTH_KILOMETERS, LENGTH_MILES)
        return int(round(visibility_mi))

    @property
    def pressure(self) -> int:
        """Return the pressure."""
        pressure_hpa = self._current[0].pres
        if self._is_metric or pressure_hpa is None:
            return pressure_hpa

        return round(convert_pressure(pressure_hpa, PRESSURE_HPA, PRESSURE_INHG), 2)

    @property
    def cloudiness(self) -> int:
        """Return the cloudiness."""
        if self._current is not None:
            return self._current[0].clouds
        return None

    @property
    def uv(self) -> int:
        """Return the UV Index."""
        if self._current is not None:
            return round(self._current[0].uv, 1)
        return None

    @property
    def aqi(self) -> int:
        """Return the Air Quality Index."""
        if self._current is not None:
            return self._current[0].aqi
        return None

    @property
    def is_night(self) -> bool:
        """Return True if after Sunset at Location."""
        if self._current is not None:
            return self._current[0].is_night
        return None

    @property
    def condition(self) -> str:
        """Return the weather condition."""
        if self._current is None:
            return None

        wcode = int(self._current[0].weather_code)

        # If Night convert to Clear Night
        if wcode == 800 and self.is_night:
            wcode = wcode * 10

        return next((k for k, v in CONDITION_CLASSES.items() if wcode in v), None,)

    @property
    def attribution(self) -> str:
        """Return the attribution."""
        return DEFAULT_ATTRIBUTION

    @property
    def device_state_attributes(self) -> Dict:
        """Return Weatherbit specific attributes."""
        return {
            ATTR_WEATHERBIT_AQI: self.aqi,
            ATTR_WEATHERBIT_CLOUDINESS: self.cloudiness,
            ATTR_WEATHERBIT_IS_NIGHT: self.is_night,
            ATTR_WEATHERBIT_PRECIPITATION: self.precipitation,
            ATTR_WEATHERBIT_WIND_GUST: self.wind_gust,
            ATTR_WEATHERBIT_UVI: self.uv,
        }

    @property
    def forecast(self) -> List:
        """Return the forecast."""
        if self._forecasts is None or len(self._forecasts) < 2:
            return None

        data = []

        for forecast in self._forecasts[1:]:
            condition = next(
                (k for k, v in CONDITION_CLASSES.items() if forecast.weather_code in v),
                None,
            )

            # Convert Wind Speed
            if self._is_metric or forecast.wind_spd is None:
                wspeed = round(float(forecast.wind_spd) * 3.6, 1)
            else:
                wspeed = round(float(forecast.wind_spd * 2.23693629), 1)

            # Convert Precipitation
            if self._is_metric or forecast.precip is None:
                precip = round(forecast.precip, 1)
            else:
                precip = round(float(forecast.precip) / 25.4, 2)

            data.append(
                {
                    ATTR_FORECAST_TIME: forecast.valid_date,
                    ATTR_FORECAST_TEMP: forecast.max_temp,
                    ATTR_FORECAST_TEMP_LOW: forecast.min_temp,
                    ATTR_FORECAST_PRECIPITATION: precip,
                    ATTR_FORECAST_CONDITION: condition,
                    ATTR_FORECAST_WIND_SPEED: wspeed,
                    ATTR_FORECAST_WIND_BEARING: forecast.wind_dir,
                }
            )

        return data
