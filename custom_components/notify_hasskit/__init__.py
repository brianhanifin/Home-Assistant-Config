""" @exlab247@gmail.com
Notification component using Firebase Cloud Messaging
Version 1.0 04 Jan 2020
Give Dust Hoof (^_^)

1. Setup a custom component

Create a folder name notify_hasskit inside Home Assistant folder in the following file structure:

.homeassistant/
|-- custom_components/
|   |-- notify_hasskit/
|       |-- __init__.py
|       |-- manifest.json
|       |-- services.yaml

2. Edit .homeassistant/configuration.yaml

Add the following line:

notify_hasskit:
  token:
    - 'Notification Token of Device 1'
    - 'Notification Token of Device 2'
    - 'Notification Token of Device 3'

3. Edit .homeassistant/automations.yaml

- alias: HassKit Test Notification
  trigger:
    - entity_id: light.light_1
      platform: state
      to: "on"
  action:
    - service: notify_hasskit.send
      data:
        device_index: 1
        title: "Light 1"
        body: "Turned On"
"""

# declare variables
DOMAIN = 'notify_hasskit'
SERVICE_SEND = 'send'
FCM_TOKEN = 'token'

# data message
CONF_DEVICE_INDEX = 'device_index' # start = 1
CONF_TITLE = 'title'
CONF_BODY= 'body'

# const data
url = "https://fcm.googleapis.com/fcm/send"
api_key = "key=AAAA7WhBA9E:APA91bGxg52oNvwKsq50pcWa-k4JGZMkXvO11m3QP0rnEVSS7D4qhEubqWBsgmVN-b4PqwsHLs3xOKXEi1qD5Nr_dsVd6NUW9VDQqaaS6hCm2pE-u5IOltOuEOkKjDpfZPPAmXzkB4DI"
header_parameters = {'Authorization': api_key, 'content-type': 'application/json',}

import requests
def send_msg(token_, title_, body_):
    data_msg = {"to": token_, "notification": {"body": body_, "title": title_}}
    status_response = requests.post(url, json = data_msg, headers = header_parameters).status_code
    if (status_response != 200): # try again
        requests.post(url, json = data_msg, headers = header_parameters)

def setup(hass, config):

    def call_send_msg(data_call):
        # get fcm_token
        list_token = config[DOMAIN][FCM_TOKEN]
        # get data msg
        index  = int(data_call.data.get(CONF_DEVICE_INDEX, 1))
        title  = str(data_call.data.get(CONF_TITLE, "Title of notification"))
        body  = str(data_call.data.get(CONF_BODY, "Body of notification"))
        index = max(1, min(index, len(list_token))) - 1
        token = list_token[index]
        # send msg
        send_msg(token, title, body)
        
    hass.services.register(DOMAIN, SERVICE_SEND, call_send_msg)
    return True
