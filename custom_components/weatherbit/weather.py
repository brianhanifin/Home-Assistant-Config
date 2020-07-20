"""Support for the Weatherbit weather service."""
import logging
from typing import Dict, List
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
    CONF_ID,
    LENGTH_METERS,
    LENGTH_MILES,
    LENGTH_KILOMETERS,
    PRESSURE_HPA,
    PRESSURE_INHG,
    TEMP_CELSIUS,
)
from homeassistant.helpers.typing import HomeAssistantType
from homeassistant.util.distance import convert as convert_distance
from homeassistant.util.pressure import convert as convert_pressure
from homeassistant.util.dt import utc_from_timestamp
import homeassistant.helpers.device_registry as dr

from .const import (
    DOMAIN,
    ATTR_WEATHERBIT_ALT_CONDITION,
    ATTR_WEATHERBIT_AQI,
    ATTR_WEATHERBIT_CLOUDINESS,
    ATTR_WEATHERBIT_IS_NIGHT,
    ATTR_WEATHERBIT_WIND_GUST,
    ATTR_WEATHERBIT_PRECIPITATION,
    ATTR_WEATHERBIT_FCST_POP,
    ATTR_WEATHERBIT_UVI,
    ATTR_WEATHERBIT_SNOW,
    ATTR_WEATHERBIT_UPDATED,
    DEFAULT_ATTRIBUTION,
    DEVICE_TYPE_WEATHER,
    CONDITION_CLASSES,
    ALT_CONDITION_CLASSES,
)
from .entity import WeatherbitEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistantType, entry: ConfigEntry, async_add_entities
) -> None:
    """Add a weather entity from mapped location."""

    fcst_coordinator = hass.data[DOMAIN][entry.entry_id]["fcst_coordinator"]
    if not fcst_coordinator.data:
        return

    cur_coordinator = hass.data[DOMAIN][entry.entry_id]["cur_coordinator"]
    if not cur_coordinator.data:
        return

    weather_entity = WeatherbitWeather(
        fcst_coordinator, cur_coordinator, entry.data, hass.config.units.is_metric,
    )

    async_add_entities([weather_entity], True)

    return True


class WeatherbitWeather(WeatherbitEntity, WeatherEntity):
    """Representation of a weather entity."""

    def __init__(self, fcst_coordinator, cur_coordinator, entries, is_metric) -> None:
        """Initialize the Weatherbit weather entity."""
        super().__init__(
            fcst_coordinator, cur_coordinator, None, entries, DEVICE_TYPE_WEATHER
        )
        self._name = f"{DOMAIN.capitalize()} {entries[CONF_ID].capitalize()}"
        self._is_metric = is_metric

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return self._name

    @property
    def temperature(self) -> int:
        """Return the temperature."""
        if self._current is not None:
            return self._current.temp
        return None

    @property
    def temperature_unit(self) -> str:
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    @property
    def humidity(self) -> int:
        """Return the humidity."""
        if self._current is not None:
            return self._current.humidity
        return None

    @property
    def wind_speed(self) -> float:
        """Return the wind speed."""
        speed_m_s = self._current.wind_spd
        if self._is_metric or speed_m_s is None:
            return round(float(speed_m_s) * 3.6, 1)

        return round(float(speed_m_s * 2.23693629), 2)

    @property
    def wind_gust(self) -> float:
        """Return the wind Gust."""
        speed_m_s = self._forecast.wind_gust_spd
        if self._is_metric or speed_m_s is None:
            return round(speed_m_s, 1)

        return round(float(speed_m_s * 2.23693629), 2)

    @property
    def wind_bearing(self) -> int:
        """Return the wind bearing."""
        if self._current is not None:
            return self._current.wind_dir
        return None

    @property
    def precipitation(self) -> float:
        """Return the precipitation."""
        if self._is_metric or self._current.precip is None:
            return round(float(self._current.precip), 1)

        return round(float(self._current.precip) / 25.4, 2)

    @property
    def ozone(self) -> float:
        """Return the ozone."""
        if self._forecast is not None:
            return round(float(self._forecast.ozone), 1)
        return None

    @property
    def visibility(self) -> float:
        """Return the visibility."""
        visibility_km = self._current.vis
        if self._is_metric or visibility_km is None:
            return visibility_km

        visibility_mi = convert_distance(visibility_km, LENGTH_KILOMETERS, LENGTH_MILES)
        return int(round(visibility_mi))

    @property
    def pressure(self) -> int:
        """Return the pressure."""
        pressure_hpa = self._current.pres
        if self._is_metric or pressure_hpa is None:
            return pressure_hpa

        return round(convert_pressure(pressure_hpa, PRESSURE_HPA, PRESSURE_INHG), 2)

    @property
    def cloudiness(self) -> int:
        """Return the cloudiness."""
        if self._current is not None:
            return self._current.clouds
        return None

    @property
    def uv(self) -> int:
        """Return the UV Index."""
        if self._current is not None:
            return round(self._current.uv, 1)
        return None

    @property
    def aqi(self) -> int:
        """Return the Air Quality Index."""
        if self._current is not None:
            return self._current.aqi
        return None

    @property
    def is_night(self) -> bool:
        """Return True if after Sunset at Location."""
        if self._current is not None:
            return self._current.is_night
        return None

    @property
    def condition(self) -> str:
        """Return the weather condition."""
        if self._current is None:
            return None

        wcode = int(self._current.weather_code)

        # If Night convert to Clear Night
        if wcode == 800 and self.is_night:
            wcode = wcode * 10

        return next((k for k, v in CONDITION_CLASSES.items() if wcode in v), None,)

    @property
    def alt_condition(self) -> str:
        """Return the alternative weather condition."""
        if self._current is None:
            return None

        wcode = int(self._current.weather_code)

        # If Night convert to night condition
        if self.is_night:
            if wcode in [800, 801, 802]:
                wcode = wcode * 10

        return next((k for k, v in ALT_CONDITION_CLASSES.items() if wcode in v), None,)

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
            ATTR_WEATHERBIT_ALT_CONDITION: self.alt_condition,
            ATTR_WEATHERBIT_IS_NIGHT: self.is_night,
            ATTR_WEATHERBIT_PRECIPITATION: self.precipitation,
            ATTR_WEATHERBIT_WIND_GUST: self.wind_gust,
            ATTR_WEATHERBIT_UVI: self.uv,
            ATTR_WEATHERBIT_UPDATED: getattr(self._current, "obs_time_local"),
        }

    @property
    def forecast(self) -> List:
        """Return the forecast."""
        if self.fcst_coordinator.data is None or len(self.fcst_coordinator.data) < 2:
            return None

        data = []

        for forecast in self.fcst_coordinator.data:
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

            # Convert Snowfall
            if self._is_metric or forecast.snow is None:
                snow = round(forecast.snow, 1)
            else:
                snow = round(float(forecast.snow) / 25.4, 2)

            data.append(
                {
                    ATTR_FORECAST_TIME: utc_from_timestamp(forecast.ts).isoformat(),
                    ATTR_FORECAST_TEMP: forecast.max_temp,
                    ATTR_FORECAST_TEMP_LOW: forecast.min_temp,
                    ATTR_FORECAST_PRECIPITATION: precip,
                    ATTR_WEATHERBIT_SNOW: snow,
                    ATTR_WEATHERBIT_FCST_POP: forecast.pop,
                    ATTR_FORECAST_CONDITION: condition,
                    ATTR_FORECAST_WIND_SPEED: wspeed,
                    ATTR_FORECAST_WIND_BEARING: forecast.wind_dir,
                }
            )

        return data
