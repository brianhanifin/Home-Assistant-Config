"""
Run the CLI config_check from a service call.

For more details about this component, please refer to the documentation at
https://github.com/custom-components/config_check
"""
import logging
from subprocess import Popen, PIPE


VERSION = '0.0.3'

NOTIFYID = '1337'

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'config_check'


async def async_setup(hass, config):
    """Set up this component."""

    _LOGGER.info('if you have ANY issues with this, please report them here:'
                 ' https://github.com/custom-components/config_check')

    _LOGGER.debug('Version %s', VERSION)

    async def run_check_service(call):
        """Set up service for manual trigger."""
        result = await run_check(str(hass.config.path()))
        hass.components.persistent_notification.async_create(
            result, 'Configuration Check Result', NOTIFYID)
    hass.services.async_register(DOMAIN, 'run', run_check_service)
    return True


async def run_check(path):
    """Run check."""
    run = None
    try:
        run = Popen(
            ["hass", "--script", "check_config", "-c", path, "-i"],
            stdin=PIPE, stdout=PIPE, stderr=PIPE)
    except Exception as error:  # pylint: disable=broad-except
        _LOGGER.debug('Could not find hass - %s', error)
    if run is None:
        try:
            run = Popen(
                ["python", "-m", "homeassistant", "--script", "check_config",
                 "-c", path, "-i"],
                stdin=PIPE, stdout=PIPE, stderr=PIPE)
        except Exception as error:  # pylint: disable=broad-except
            _LOGGER.debug('Could not find homeassistant - %s', error)
    if run is None:
        _LOGGER.critical('Could not find hass/homeassistant')
        return 'Could not find hass/homeassistant'
    result, err = run.communicate()
    _LOGGER.debug(result)
    _LOGGER.debug(err)
    result = result.decode()
    result = result.replace(
        'INFO:homeassistant.util.package:Attempting install of colorlog==4.0.2\n', '')
    result = result.replace('Testing configuration at /config\n', '')
    result = result.replace('Successful config (all)', '')
    result = result.replace('\n  homeassistant:', '')

    result = result.replace('Failed config', '**Failed config**')

    result = result.split('?')[0]

    result = await remove_last_line_from_string(result)

    _LOGGER.debug(result)

    if result == '':
        result = "\nConfiguration is OK!\n"

    return result


async def remove_last_line_from_string(string):
    """Remove last line from string."""
    result = string[:string.rfind('\n')]
    return result
