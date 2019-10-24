"""
Run the CLI config_check from a service call.

For more details about this component, please refer to the documentation at
https://github.com/custom-components/config_check
"""
import logging
from subprocess import Popen, PIPE

NOTIFYID = "1337"

_LOGGER = logging.getLogger(__name__)

DOMAIN = "config_check"


async def async_setup(hass, config):
    """Set up this component."""

    _LOGGER.info(
        """
-------------------------------------------------------------------
CONFIG CHECK

This is a custom integration
If you have any issues with this you need to open an issue here:
https://github.com/custom-components/config_check
-------------------------------------------------------------------
"""
    )

    async def run_check_service(call):
        """Set up service for manual trigger."""
        result = await run_check(str(hass.config.path()))
        hass.components.persistent_notification.async_create(
            result, "Configuration Check Result", NOTIFYID
        )
        if result == "\nConfiguration is OK!\n":
            finish_service = call.data.get("service")
            finish_service_data = call.data.get("service_data", {})
            if finish_service is not None:
                domain = finish_service.split(".")[0]
                service = finish_service.split(".")[1]
                await hass.services.async_call(domain, service, finish_service_data)

    hass.services.async_register(DOMAIN, "run", run_check_service)
    return True


async def run_check(path):
    """Run check."""
    run = None
    try:
        run = Popen(
            ["hass", "--script", "check_config", "-c", path, "-i"],
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
        )
    except Exception as error:  # pylint: disable=broad-except
        _LOGGER.debug("Could not find hass - %s", error)
    if run is None:
        try:
            run = Popen(
                [
                    "python",
                    "-m",
                    "homeassistant",
                    "--script",
                    "check_config",
                    "-c",
                    path,
                    "-i",
                ],
                stdin=PIPE,
                stdout=PIPE,
                stderr=PIPE,
            )
        except Exception as error:  # pylint: disable=broad-except
            _LOGGER.debug("Could not find homeassistant - %s", error)
    if run is None:
        _LOGGER.critical("Could not find hass/homeassistant")
        return "Could not find hass/homeassistant"
    result, err = run.communicate()
    result = result.decode()
    _LOGGER.debug(result)
    _LOGGER.debug(err)
    if "Failed config" in result:
        result = clear_result(result)
        result = remove_last_line_from_string(result)
        _LOGGER.debug(result)
    else:
        result = "\nConfiguration is OK!\n"

    return result


def remove_last_line_from_string(string):
    """Remove last line from string."""
    result = string[: string.rfind("\n")]
    return result


def clear_result(string):
    """Clear out unwanted stuff from the result."""
    clear_out = [
        "INFO:homeassistant.util.package:Attempting install of colorlog==4.0.2\n",
        "Testing configuration at /config",
        "homeassistant:",
        "General Errors:",
        "[0m",
        "[01m",
        "[01;37m",
        "[01;31m",
        "[31m",
        "      ",
    ]
    string = string.split("Successful config (all)")[0]
    for clear in clear_out:
        string = string.replace(clear, "")

    string = string.replace("Failed config", "**Failed config**")

    return string.split("?")[0]
