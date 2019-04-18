# Install the Rainforest Component
Place `__init__.py` and `sensor.py` in `config\custom_components\rainforest\`


## Overview
To use your Rainforest Automation EMU-2™ Energy Monitoring Unit in your installation, add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
sensor:
  - platform: rainforest
    port: '/dev/ttyACM0'
```

## Configuraion

### port:
  * description: The comm port which the meter is connected to.
  * required: true
  * type: string

### name:
  * description: The name to use when displaying this sensor.
  * required: false
  * type: string

## Reference Material
 * https://github.com/smakonin/RAEdataset/blob/master/EMU2_reader.py
 * https://github.com/home-assistant/home-assistant/blob/master/homeassistant/components/sensor/serial.py
 * https://home-assistant.io/components/sensor.date_countdown/
 * https://github.com/rainforestautomation/Emu-Serial-API
