"""Base Entity for Weatherbit."""

from homeassistant.helpers.entity import Entity
import homeassistant.helpers.device_registry as dr

from homeassistant.const import (
    ATTR_ATTRIBUTION,
    CONF_LATITUDE,
    CONF_LONGITUDE,
)
from .const import (
    DOMAIN,
    DEFAULT_BRAND,
    DEFAULT_ATTRIBUTION,
    DEVICE_TYPE_WEATHER,
)


class WeatherbitEntity(Entity):
    """Base class for Weatherbit Entities."""

    def __init__(
        self, fcst_coordinator, cur_coordinator, alert_coordinator, entries, entity
    ):
        """Initialize the Weatherbit Entity."""
        super().__init__()
        self.fcst_coordinator = fcst_coordinator
        self.cur_coordinator = cur_coordinator
        self.alert_coordinator = alert_coordinator
        self.entries = entries
        self._entity = entity
        self._device_key = (
            f"{self.entries[CONF_LATITUDE]}_{self.entries[CONF_LONGITUDE]}"
        )
        if self._entity == DEVICE_TYPE_WEATHER:
            self._unique_id = self._device_key
        else:
            self._unique_id = f"{self._device_key}_{self._entity}"

    @property
    def unique_id(self):
        """Return a unique ID."""
        return self._unique_id

    @property
    def _forecast(self):
        """Return Forecast Data Array."""
        return self.fcst_coordinator.data[0]

    @property
    def _current(self):
        """Return Current Data."""
        return self.cur_coordinator.data[0]

    @property
    def _alerts(self):
        """Return Current Data."""
        if self.alert_coordinator is not None:
            return self.alert_coordinator.data[0]

    @property
    def _latitude(self):
        """Return Latitude."""
        return self.entries[CONF_LATITUDE]

    @property
    def device_info(self):
        return {
            "connections": {(dr.CONNECTION_NETWORK_MAC, self._device_key)},
            "manufacturer": DEFAULT_BRAND,
            "model": "Weatherbit.io API",
            "via_device": (DOMAIN, self._device_key),
        }

    @property
    def available(self):
        """Return if entity is available."""
        return self.cur_coordinator.last_update_success

    async def async_added_to_hass(self):
        """When entity is added to hass."""
        self.async_on_remove(
            self.cur_coordinator.async_add_listener(self.async_write_ha_state)
        )
        self.async_on_remove(
            self.fcst_coordinator.async_add_listener(self.async_write_ha_state)
        )
        if self.alert_coordinator is not None:
            self.async_on_remove(
                self.alert_coordinator.async_add_listener(self.async_write_ha_state)
            )
