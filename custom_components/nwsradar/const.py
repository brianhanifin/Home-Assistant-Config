"""Constants for NWS Radar integration."""
DOMAIN = "nwsradar"

CONF_STYLE = "style"
CONF_STATION = "station"
CONF_LOOP = "loop"
CONF_TYPE = "type"
CONF_NAME = "name"

STYLES = ["Standard", "Enhanced", "Mosaic"]

RADAR_TYPES = {
    "Composite Reflectivity": "NCR",
    "Base Reflectivity 124 nm": "N0R",
    "Base Reflectivity 248 nm": "N0Z",
    "Storm Relative Motion": "N0S",
    "One-Hour Precipitation": "N1P",
    "Storm Total Precipitation": "NTP",
}
DEFAULT_RADAR_TYPE = "Composite Reflectivity"

DATA_COORDINATOR = "coordinator"
DATA_CAM = "cam"
