"""Weatherbit Sensors for Home Assistant."""

import logging
from typing import Dict, List

from homeassistant.helpers.entity import Entity
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import HomeAssistantType
from homeassistant.util.pressure import convert as convert_pressure
from homeassistant.util.distance import convert as convert_distance
from homeassistant.const import (
    ATTR_ATTRIBUTION,
    LENGTH_METERS,
    LENGTH_MILES,
    LENGTH_KILOMETERS,
    PRESSURE_HPA,
    PRESSURE_INHG,
    TEMP_CELSIUS,
    SUN_EVENT_SUNSET,
    SUN_EVENT_SUNRISE,
)
from homeassistant.components.weather import (
    ATTR_FORECAST_CONDITION,
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_TEMP,
    ATTR_FORECAST_TEMP_LOW,
    ATTR_FORECAST_TIME,
    ATTR_FORECAST_WIND_BEARING,
    ATTR_FORECAST_WIND_SPEED,
)
from .const import (
    DOMAIN,
    ATTR_WEATHERBIT_ALERTS,
    ATTR_WEATHERBIT_CLOUDINESS,
    ATTR_WEATHERBIT_UPDATED,
    ATTR_WEATHERBIT_FCST_POP,
    ATTR_WEATHERBIT_WEATHER_TEXT,
    ATTR_WEATHERBIT_WEATHER_ICON,
    ATTR_WEATHERBIT_SNOW,
    DEFAULT_ATTRIBUTION,
    DEVICE_TYPE_TEMPERATURE,
    DEVICE_TYPE_WIND,
    DEVICE_TYPE_HUMIDITY,
    DEVICE_TYPE_RAIN,
    DEVICE_TYPE_SNOW,
    DEVICE_TYPE_PRESSURE,
    DEVICE_TYPE_DISTANCE,
    TYPE_SENSOR,
    TYPE_FORECAST,
    TYPE_ALERT,
    CONDITION_CLASSES,
    CONF_ADD_SENSORS,
)
from .entity import WeatherbitEntity


SENSORS = {
    "temp": ["Temperature", DEVICE_TYPE_TEMPERATURE, "thermometer"],
    "wind_spd": ["Wind Speed", DEVICE_TYPE_WIND, "weather-windy"],
    "app_temp": ["Apparent Temperature", DEVICE_TYPE_TEMPERATURE, "thermometer"],
    "humidity": ["Humidity", DEVICE_TYPE_HUMIDITY, "water-percent"],
    "pres": ["Pressure", DEVICE_TYPE_PRESSURE, "gauge"],
    "slp": ["Sea Level Pressure", DEVICE_TYPE_PRESSURE, "gauge"],
    "clouds": ["Cloud Coverage", "%", "cloud-outline"],
    "solar_rad": ["Solar Radiation", "W/m^2", "weather-sunny"],
    "wind_cdir": ["Wind Direction", "", "compass-outline"],
    "wind_dir": ["Wind Bearing", "°", "compass-outline"],
    "dewpt": ["Dewpoint", DEVICE_TYPE_TEMPERATURE, "thermometer"],
    "vis": ["Visibility", DEVICE_TYPE_DISTANCE, "eye-outline"],
    "precip": ["Rain Rate", DEVICE_TYPE_RAIN, "weather-rainy"],
    "uv": ["UV Index", "UVI", "weather-sunny-alert"],
    "aqi": ["Air Quality", "AQI", "hvac"],
    "weather_text": ["Description", "", "text-short"],
    "weather_icon": ["Icon Code", "", "simple-icons"],
    "beaufort_value": ["Beaufort Value", "", "weather-tornado"],
    "beaufort_text": ["Beaufort Text", "", "weather-tornado"],
    "snow": ["Snow Rate", DEVICE_TYPE_SNOW, "weather-snowy-heavy"],
}

ALERTS = {
    "weather_alerts": ["Weather Alerts", "", "alert"],
}

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistantType, entry: ConfigEntry, async_add_entities
) -> None:
    """Setup the Weatherbit sensor platform."""

    # Exit if user did deselect sensors and alerts on config
    if (
        not entry.data[CONF_ADD_SENSORS]
        and hass.data[DOMAIN][entry.entry_id]["alert_coordinator"] is None
    ):
        return

    # Get the Data Coordinators used
    fcst_coordinator = hass.data[DOMAIN][entry.entry_id]["fcst_coordinator"]
    if not fcst_coordinator.data:
        return

    cur_coordinator = hass.data[DOMAIN][entry.entry_id]["cur_coordinator"]
    if not cur_coordinator.data:
        return

    alert_coordinator = hass.data[DOMAIN][entry.entry_id]["alert_coordinator"]

    sensors = []

    # Add Sensors if selected in Config
    if entry.data[CONF_ADD_SENSORS]:
        for sensor in SENSORS:
            sensors.append(
                WeatherbitSensor(
                    fcst_coordinator,
                    cur_coordinator,
                    alert_coordinator,
                    entry.data,
                    sensor,
                    hass.config.units.is_metric,
                    TYPE_SENSOR,
                    0,
                )
            )
        cnt = 0

        for forecast in fcst_coordinator.data[:7]:
            sensors.append(
                WeatherbitSensor(
                    fcst_coordinator,
                    cur_coordinator,
                    alert_coordinator,
                    entry.data,
                    forecast,
                    hass.config.units.is_metric,
                    TYPE_FORECAST,
                    cnt,
                )
            )
            cnt += 1

    # Add alerts if selected in Config
    if alert_coordinator is not None:
        for sensor in ALERTS:
            sensors.append(
                WeatherbitSensor(
                    fcst_coordinator,
                    cur_coordinator,
                    alert_coordinator,
                    entry.data,
                    sensor,
                    hass.config.units.is_metric,
                    TYPE_ALERT,
                    0,
                )
            )
    if sensors != []:
        async_add_entities(sensors, True)
    else:
        return

    return True


class WeatherbitSensor(WeatherbitEntity, Entity):
    """Implementation of Weatherbit sensor."""

    def __init__(
        self,
        fcst_coordinator,
        cur_coordinator,
        alert_coordinator,
        entries,
        sensor,
        is_metric,
        sensor_type,
        index,
    ):
        """Initialize Weatherbit sensor."""
        super().__init__(
            fcst_coordinator, cur_coordinator, alert_coordinator, entries, sensor
        )
        self._sensor = sensor
        self._sensor_type = sensor_type
        self._is_metric = is_metric
        self._index = index

        if self._sensor_type == TYPE_SENSOR:
            self._name = f"{DOMAIN.capitalize()} {SENSORS[self._sensor][0]}"
            self._unique_id = f"{self._device_key}_{self._sensor}"
            self._device_class = SENSORS[self._sensor][1]
        elif self._sensor_type == TYPE_ALERT:
            self._name = f"{DOMAIN.capitalize()} {ALERTS[self._sensor][0]}"
            self._unique_id = f"{self._device_key}_{self._sensor}"
            self._device_class = ALERTS[self._sensor][1]
        else:
            self._name = f"{DOMAIN.capitalize()} Forecast Day {self._index + 1}"
            self._unique_id = f"{self._device_key}_forecast_day{self._index + 1}"
            self._device_class = ""
            self._condition = next(
                (
                    k
                    for k, v in CONDITION_CLASSES.items()
                    if getattr(self.fcst_coordinator.data[self._index], "weather_code")
                    in v
                ),
                None,
            )
            if self._condition == "partlycloudy":
                self._weather_icon = "partly-cloudy"
            else:
                self._weather_icon = self._condition

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        if self._sensor_type == TYPE_SENSOR:
            value = getattr(self._current, self._sensor)
            if self._device_class == DEVICE_TYPE_WIND:
                if self._is_metric:
                    return round(value, 1)
                else:
                    return round(float(value * 2.23693629), 2)
            elif self._device_class == DEVICE_TYPE_PRESSURE:
                if self._is_metric:
                    return value
                else:
                    return round(
                        convert_pressure(value, PRESSURE_HPA, PRESSURE_INHG), 2
                    )
            elif (
                self._device_class == DEVICE_TYPE_RAIN
                or self._device_class == DEVICE_TYPE_SNOW
            ):
                if self._is_metric:
                    return round(float(value), 1)
                else:
                    return round(float(value) / 25.4, 2)
            elif self._device_class == DEVICE_TYPE_DISTANCE:
                if self._is_metric:
                    return value
                else:
                    return int(
                        float(convert_distance(value, LENGTH_KILOMETERS, LENGTH_MILES))
                    )
            elif self._device_class == "UVI":
                return round(float(value), 1)
            else:
                return value
        elif self._sensor_type == TYPE_ALERT:
            return getattr(self._alerts, "alert_count")
        else:
            return self._condition

    @property
    def icon(self):
        """Return icon for sensor."""
        if self._sensor_type == TYPE_SENSOR:
            return f"mdi:{SENSORS[self._sensor][2]}"
        elif self._sensor_type == TYPE_ALERT:
            return f"mdi:{ALERTS[self._sensor][2]}"
        else:
            return f"mdi:weather-{self._weather_icon}"

    @property
    def unit_of_measurement(self):
        """Return the units of measurement."""
        if self._sensor_type == TYPE_SENSOR:
            if self._device_class == DEVICE_TYPE_TEMPERATURE:
                return TEMP_CELSIUS
            elif self._device_class == DEVICE_TYPE_WIND:
                return "m/s" if self._is_metric else "mph"
            elif self._device_class == DEVICE_TYPE_PRESSURE:
                return "hPa" if self._is_metric else "inHg"
            elif self._device_class == DEVICE_TYPE_HUMIDITY:
                return "%"
            elif self._device_class == DEVICE_TYPE_RAIN:
                return "mm/hr" if self._is_metric else "in/hr"
            elif self._device_class == DEVICE_TYPE_SNOW:
                return "mm/hr" if self._is_metric else "in/hr"
            elif self._device_class == DEVICE_TYPE_DISTANCE:
                return "km" if self._is_metric else "mi"
            else:
                return self._device_class

    @property
    def alerts(self) -> List:
        if self._sensor_type != TYPE_ALERT:
            return

        if self.alert_coordinator.data is None:
            return None

        alert_data = []
        for alert in self.alert_coordinator.data:
            alert_data.append(
                {
                    "city_name": alert.city_name,
                    "title": alert.title,
                    "description": alert.description,
                    "severity": alert.severity,
                    "effective_local": alert.effective_local,
                    "expires_local": alert.expires_local,
                    "uri": alert.uri,
                    "regions": alert.regions,
                }
            )
        return alert_data

    @property
    def device_state_attributes(self):
        """Return Weatherbit specific attributes."""
        if self._sensor_type == TYPE_SENSOR:
            if self._sensor == "solar_rad":
                return {
                    ATTR_ATTRIBUTION: DEFAULT_ATTRIBUTION,
                    ATTR_WEATHERBIT_UPDATED: getattr(self._current, "obs_time_local"),
                    "dhi": getattr(self._current, "dhi"),
                    "dni": getattr(self._current, "dni"),
                    "ghi": getattr(self._current, "ghi"),
                    "elev_angle": getattr(self._current, "elev_angle"),
                    "h_angle": getattr(self._current, "h_angle"),
                    SUN_EVENT_SUNRISE: getattr(self._current, "sunrise"),
                    SUN_EVENT_SUNSET: getattr(self._current, "sunset"),
                }
            else:
                return {
                    ATTR_ATTRIBUTION: DEFAULT_ATTRIBUTION,
                    ATTR_WEATHERBIT_UPDATED: getattr(self._current, "obs_time_local"),
                }
        elif self._sensor_type == TYPE_ALERT:
            return {
                ATTR_ATTRIBUTION: DEFAULT_ATTRIBUTION,
                ATTR_WEATHERBIT_ALERTS: self.alerts,
            }
        else:
            _temp = getattr(self.fcst_coordinator.data[self._index], "max_temp")
            if self._is_metric:
                temp = _temp
            else:
                temp = round(float((_temp * 1.8) + 32), 1)

            _tempmin = getattr(self.fcst_coordinator.data[self._index], "min_temp")
            if self._is_metric:
                tempmin = _tempmin
            else:
                tempmin = round(float((_tempmin * 1.8) + 32), 1)

            _wspeed = getattr(self.fcst_coordinator.data[self._index], "wind_spd")
            if self._is_metric:
                wspeed = round(float(_wspeed) * 3.6, 1)
            else:
                wspeed = round(float(_wspeed * 2.23693629), 1)

            _precip = getattr(self.fcst_coordinator.data[self._index], "precip")
            if self._is_metric:
                precip = round(float(_precip), 1)
            else:
                precip = round(float(_precip) / 25.4, 2)

            _snow = getattr(self.fcst_coordinator.data[self._index], "snow")
            if self._is_metric:
                snow = round(float(_snow), 1)
            else:
                snow = round(float(_snow) / 25.4, 2)

            return {
                ATTR_ATTRIBUTION: DEFAULT_ATTRIBUTION,
                ATTR_FORECAST_TIME: getattr(
                    self.fcst_coordinator.data[self._index], "local_time"
                ),
                ATTR_FORECAST_TEMP: temp,
                ATTR_FORECAST_TEMP_LOW: tempmin,
                ATTR_FORECAST_PRECIPITATION: precip,
                ATTR_WEATHERBIT_SNOW: snow,
                ATTR_WEATHERBIT_CLOUDINESS: getattr(
                    self.fcst_coordinator.data[self._index], "clouds"
                ),
                ATTR_WEATHERBIT_FCST_POP: getattr(
                    self.fcst_coordinator.data[self._index], "pop"
                ),
                ATTR_FORECAST_WIND_SPEED: wspeed,
                ATTR_FORECAST_WIND_BEARING: getattr(
                    self.fcst_coordinator.data[self._index], "wind_dir"
                ),
                ATTR_WEATHERBIT_WEATHER_TEXT: getattr(
                    self.fcst_coordinator.data[self._index], "weather_text"
                ),
                ATTR_WEATHERBIT_WEATHER_ICON: getattr(
                    self.fcst_coordinator.data[self._index], "weather_icon"
                ),
            }
