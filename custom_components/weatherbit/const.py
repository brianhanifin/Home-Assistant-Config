"""Constants in weatherbit component."""
import logging

from homeassistant.components.weather import DOMAIN as WEATHER_DOMAIN

ATTR_WEATHERBIT_AQI = "aqi"
ATTR_WEATHERBIT_CLOUDINESS = "cloudiness"
ATTR_WEATHERBIT_IS_NIGHT = "is_night"
ATTR_WEATHERBIT_WIND_GUST = "wind_gust"
ATTR_WEATHERBIT_PRECIPITATION = "precipitation"
ATTR_WEATHERBIT_UVI = "uv_index"

DOMAIN = "weatherbit"

ENTITY_ID_SENSOR_FORMAT = WEATHER_DOMAIN + "." + DOMAIN + "_{}"

DEFAULT_ATTRIBUTION = "Data provided by Weatherbit.io"

LOGGER = logging.getLogger(__package__)
