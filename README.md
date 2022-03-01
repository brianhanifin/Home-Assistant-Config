# Hanifin smart home

| brianhanifin/home-assistant-config | Home Assistant Community |
| :---: | :---: |
| [![Home Assistant Version][ha-version-shield]][ha-version] [![Github Action Status][github-build-status-shield]][github-build-status] [![Github Linter Status][github-linter-status-shield]][github-linter-status] | [![Community Forum][discourse-shield]][discourse]
| [![Last Commit][github-last-commit]][github-master] [![GitHub Activity][commits-shield]][commits] [![Lines of code count][code-lines-shield]][code-link] | [![Discord][discord-shield]][discord] |

## Smart home articles

I write instructional articles on [brianhanifin.com](https://brianhanifin.com/). Topics primarily revolve around Home Assistant and ESPHome code and devices, but I also I have written about my HomeLab server setup.

---

## An occasionally updated summary of our smart home
I started using Home Assistant in the spring of 2018 when we outgrew the limited automations on Apple's HomeKit platform. Our Home Assistant initially included many HomeKit smart plugs our collection of smart lights, switches, plugs, cameras, and sensors. Since we have added many devices that use protocols like Zigbee and Z-Wave and even several custom built electronic modules.

Home Assistant now manages our smart home devices with lots of intelligence handled by automations. It is important that our devices can be controlled by standard wall switches, but we also use Google Nest speakers to control our devices with our voice. Not only can we talk to Google, but she can let us know when a laundry cycle, 3D Print, or laser cutting job is complete.

## User interface

### Physical buttons
We use a variety of physical switches from hard-wired to battery powered.

#### In-wall dimmers and switches
These can be used to control dumb lights. However, some devices allow you pass constant power so you can control smart bulbs with Home Assistant. For example a switch in my Dining Room leaves power to my Hue bulbs so I can turn the lights on with my voice or the physical wall switch.

<span style="float:left">![bedroom_switches]</span>
#### Bedside toggle switches
A battery powered double switch to my wife's bedside table. Single clicks toggle the lights on either side of our bed. While a double click toggles the bedroom fan, or the sound machine.

### Google nest speakers and displays
We can also interact with our devices with Google Nest speakers in all of the major rooms of the house.

Our Google Nest also make announcements when something needs our immediate attention. For example: when it is time to leave for school, or its time to start cooking dinner because mom's on her way home from work.

### Tablet reference user interface
We have a 7-inch Amazon tablet in the Kitchen which displays useful information such as our family calendar and which child's turn is it do the dishes this week.

### Mobile user interface
I exclusively Interact with Home Assistant with my phone (or computer when coding). If no one else needs to bother with it, I have done a good job!  :smirk:

---

## Smart home devices

> Disclosure: This article may contain affiliate links. If you decide to make a purchase, I'll make a small commission at no extra cost to you.

### Lutron caseta
Device recommendations: [dimmer](https://amzn.to/3pHXJth), [pico remote](https://amzn.to/2OYVHZ4), [dimmer and pico remote](https://amzn.to/3unpD0Y), [Lutron caseta pro bridge](https://amzn.to/3aH1pqO)

In-wall dimmer switches and in-wall (or handheld) wireless remotes. Get the [Lutron caseta pro bridge](https://amzn.to/3aH1pqO) so you can us your pico remotes with Home Assistant to control any device in your house! The standard bridge is less expensive but you cannot watch for pico remote button press events.

#### Project ideas
1. Add a battery powered pico remote next to a room which doesn't have a wall switch! Control a smart bulb by any manufacturer! My Living Room was lacking a switch, but I cut a little hole in drywall and now it does! :beers:
2. Replace a dumb wired light switch or dimmer with a caseta dimmer so Home Assistant can automatically turn the lights on at night when a motion sensor detects you have entered the room!
3. Use Home Assistant to brighten the lights gradually to help you wake up in the morning.

### Inovelli red series switches and dimmers
Device recommendations: [Red series dimmer](https://amzn.to/2ZY73i3), [Red series switch](https://amzn.to/3r2WtT5), [Red series fan & light switch](https://amzn.to/3q0yB12)

Inovelli z-wave devices are high quality and they really care about our niche community. The red series switches handle double, triple, quadruple, and event quintuple click events. These even have a led light strip on the right side which we use different color and animations to indicate the state of things around the house.

#### Project ideas
1. **Multi-click actions!** 2x click to turn on/off the bright floor lamp, 3x click to turn on/off the floor fan, 4x click to activate your "goodnight" scene, 5x click to activate guest mode on your way to answer the door!<br>
*See my automation: [automations/buttons/zwjs_button_click.yaml](https://github.com/brianhanifin/Home-Assistant-Config/blob/master/automations/buttons/zwjs_button_click.yaml)*
2. **House status indicator** Use the LED strip to indicate when the garage is open, or the alarm is disarmed.<br>
*See my article: "[Inovelli red series status LED update](https://brianhanifin.com/posts/inovelli-red-series-status-led-update/)"*

### Philips hue bulbs
Device recommendations: [starter Kit](https://amzn.to/37AqeTq) (3 color bulbs, battery dimmer, & hub)

The Hue ecosystem is easy to get setup with Home Assistant. We primarily use their tunable white bulbs for plug in floor and table lamps, but we do have 9 colored bulbs in our dining room chandelier for holiday fun.

#### Project ideas
1. Use these bulbs to make your plug in lamps controllable by Home Assistant.
2. Create a realistic sunrise to wakeup in the morning using the tunable white light.

### Smoke + carbon monoxide detectors

Device recommendation: [first alert z-wave 2-in-1 smoke detector & carbon monoxide alarm](https://amzn.to/3r0RjGV)

Thanks to Carlo's article "[PSA: CHECK OUT YOUR SMOKE DETECTORS (ONCE EVERY 10 YEARS)][carlo-blog-smoke]" I realized that I had lived in my house for almost 11 years, and we were due for new smoke detectors. So I replaced them with new First Alert zcombo z-wave smoke detectors.

#### Project ideas:
1. **Safety alert!** Have Home Assistant alert you which detector sensed the smoke so you can decide whether to try to put it out, or get to safety!

### Xiaomi aqara zigbee smart home devices
Device recommendations: [wireless buttons](https://amzn.to/3q4jd3w), [motion & luminance sensors](https://amzn.to/3q0OOTK), [temperature & humidity sensors](https://amzn.to/2ZYWV8I), [door & window sensors](https://amzn.to/2ZWptjl), [leak sensors](https://amzn.to/3r1bYef), [vibration sensors](https://amzn.to/2ZUvrBl)
Hub recomendations: [Phoscon conbee II USB gateway](https://amzn.to/2Mz3jk8), [Aqara homekit hub](https://amzn.to/37TN6xv), [Aqara starter kit: hub, plug, button, motion, door/window](https://amzn.to/2O6STIO)

This chinese company makes a lot of very useful and inexpensive wireless smart home products. At first I used their Zigbee smart hub to get these devices to talk to Home Assistant. However I now use a USB stick connected to my server to communicate with all of my Zigbee devices.

#### Project ideas
1. **Door and window sensors**: Stick door and window sensors on doors and windows around your house and have Home Assistant remind you to close the doors and windows when it starts to get warm outside.
2. **Motion lights**: stick a motion sensor in your<br>
  2a. Kitchen to turn on an LED strip under your cabinets to give yourself a nightlight when getting water in the middle of the night.<br>
  2b. Bedroom to light a dim path to the bathroom.
3. **Flood damage alert!** Place leak sensors under your all sinks, dishwasher, clothes washer, refrigerator, and water heater. Setup an alert to notify you where the leak is. This will give you valuable time to stop major flood damage!
4. **Medicine logger**: stick a wireless button inside the medicine cabinet to log when you gave seizure medicine to your dog.
5. **Automatic bathroom exhaust**: use a temperature & humidity sensor to automatically turn on your exhaust fan and turn it back off when the humidity drops again.

## DIY smart home devices

I have flashed the below devices with ESPHome firmware which I have full control 
over! You can see my code at my [esphome-config GitHub repository][esphome-config].

### Shelly 1 boards
Device recommendations: shelly 1 ([1 pack](https://amzn.to/3qKTyhI), [2 pack](https://amzn.to/3bw9bmN)), [shelly 2](https://amzn.to/37Aq7qY)

These devices are great for shoving in a box behind a light switch to add smarts.

#### Project ideas
1. **Hue bulb functional light switch**: my dining room has a 9 bulb chandelier, this provides constant power, while allowing the switch to remain functional.
2. **Smart bathroom exhaust fan**<br>
*2a.* turns the fan off after 10 minutes when manually turned on (*note: a battery powered motion sensor resets the countdown*).<br>
*2b.* turns the fan on then back off when the humidity is up due to a shower (*note: a battery powered humidity sensor in the bathroom is compared to one in a neighboring room*).
3. **Garage door controller**: I plan to replace the cloud based chamberlain MyQ controller soon using [the hook up's video for reference ](https://www.youtube.com/watch?v=WEZUxXNiERQ).

### SonOff S31 plugs
Device recommendations: [S31](https://amzn.to/2OOEilB), [S31 lite](https://amzn.to/2NMhi6i)

The SonOff S31 is a reliable wi-fi controlled smart switch which can be flashed with Tasmota or ESPHome if you wish. The original S31 has power monitoring built in, while the new S31 lite omits that for a discount.

#### S31 power monitoring project ideas
*Note: the relay can be left always on to put these in a monitor only mode.*
1. Monitor your washing machine so Home Assistant can notify you when your wash is ready to be hung up or moved to the dryer! No more stinky clothes!
2. Monitor your dishwasher or clothes dryer.
3. Monitor your 3D Printer or Laser Cutter to let you know when it is time to check out that thing you just created!

#### S31 lite project ideas
1. Plug one of these into every floor and table fan you own and just ask your Google or Alexa to *"turn on the bedroom fan!"*.
2. Plug one into a sound machine to help you sleep at night. Have Home Assistant automatically start this when your phone starts charging for the night.

### Presence detection

#### Life360 integration
I use [Life360](https://www.life360.com/) for presence tracking on my son's, wife's, and my phone. This has made me comfortable enough to do things like having Home Assistant close the garage door if one of us leaves the home zone. This covers us for those few times we may forget to close the door before driving away! :)

#### Ubiquiti UniFi integration
For extended family visitors I use the [Home Assistant Ubiquiti UniFi integration](https://www.home-assistant.io/integrations/unifi/#presence-detection) to track when their phones are connected to my wireless access points.

#### Guest mode helper
Finally, I have a "Guest Mode" input_boolean setup as both a trigger and a condition on many of my lighting and front door locking automations.

## Wireless communications

### Wi-fi: Ubiquiti Unifi
Device recommendations: [Unifi 6 lite access point](https://amzn.to/3q1OUut) (wi-fi 6), [Unifi AC-PRO access point](https://amzn.to/2NMc1vW) (802.11ac, I have 3 of these), [Unifi security gateway](https://amzn.to/2NEbooj)

Eventually you outgrow even the fanciest home wi-fi setup. There were just too many devices for my Netgear orbi mesh networking system to handle, so I had to upgrade to a business grade solution.

Pros:
* Rock solid wi-fi all throughout the downstairs.
* Household members don't complain about the wi-fi anymore!
* Long ethernet cable runs make all access points equally fast!

Cons:
* Requires a long ethernet cable run to each access point. (But also a "pro"... see the last point above.)

### Zigbee
Recommendation: [Phoscon conbee II USB gateway](https://amzn.to/2Mz3jk8)

Home Assistant's ZHA integration directly runs all of my zigbee devices. This includes all of my philips hue bulbs and all of my Xiaomi Aqara sensors!

### Z-wave
Recommendation: [Aeotec Z-Stick Gen5 Plus](https://amzn.to/3kw7YzO)

As of February 2021 Home Assistant's Z-Wave JS integration directly runs all of my z-wave devices. To be precise I am running [Zwavejs2Mqtt](https://zwave-js.github.io/zwavejs2mqtt/#/)) with MQTT disabled so I can make use of the z-wave device management UI built in. This includes several in-wall switches and dimmers, smoke detectors, and a bulb.

## Technical details

Our Home Assistant install has approximately **1244 total entities**, 
including **676 sensors**.

<details><summary>24 Custom integrations</summary>

#### [Adaptive Lighting v1.0.14](https://github.com/basnijholt/adaptive-lighting#readme)

Adaptive Lighting custom component for Home Assistant
Authors: [@basnijholt](https://github.com/basnijholt), [@RubenKelevra](https://github.com/RubenKelevra).


#### [Anniversaries v4.5.0](https://github.com/pinkywafer/Anniversaries)

Anniversary Countdown Sensor for Home Assistant
Authors: [@pinkywafer](https://github.com/pinkywafer).


#### [Average Sensor v2.2.1](https://github.com/Limych/ha-average)

Average Sensor for Home Assistant
Authors: [@Limych](https://github.com/Limych).


#### [Battery Simulation v1.0](https://github.com/hif2k1/battery_sim/)


Authors: [@hif2k1](https://github.com/hif2k1).


#### [Breaking Changes v21.12.0](https://github.com/custom-components/breaking_changes)

Component to show potential breaking_changes in the current published version based on your loaded components
Authors: [@ludeeus](https://github.com/ludeeus).


#### [Config Check v0.1.1](https://github.com/custom-components/config_check)

Run the CLI config_check from a service call.
Authors: [@ludeeus](https://github.com/ludeeus).


#### [Fontawesome icons v2.1.5](https://github.com/thomasloven/hass-fontawesome)





#### [Frigate v2.2.2](https://github.com/blakeblackshear/frigate)

Frigate integration for Home Assistant
Authors: [@blakeblackshear](https://github.com/blakeblackshear).


#### [Generate readme v0.4.0](https://github.com/custom-components/readme)


Authors: [@ludeeus](https://github.com/ludeeus).


#### [Google Home v1.9.8](https://github.com/leikoilja/ha-google-home)

Home Assistant Google Home custom component
Authors: [@leikoilja](https://github.com/leikoilja), [@DurgNomis-drol](https://github.com/DurgNomis-drol), [@ArnyminerZ](https://github.com/ArnyminerZ), [@KapJI](https://github.com/KapJI).


#### [Home Assistant Community Store (HACS) v1.23.0](https://hacs.xyz/docs/configuration/start)

HACS gives you a powerful UI to handle downloads of all your custom needs.
Authors: [@ludeeus](https://github.com/ludeeus).


#### [HASS.Agent Notifier v2021.12.21](https://github.com/LAB02-Research/HASS.Agent-Notifier)


Authors: [@LAB02-Admin](https://github.com/LAB02-Admin).


#### [Holidays v1.7](https://github.com/bruxy70/Holidays/)

📅 Custom Home Assistant integration for public holidays - also used for garbage_collection integration to automatically move scheduled events that fall on a public holiday (by an automation blueprint)
Authors: [@bruxy70](https://github.com/bruxy70).


#### [Lovelace Notify v1.0.0]()

Lovelace notification / alert component for Home Assistant
Authors: [@rr326](https://github.com/rr326).


#### [Rainforest v0.2.2](https://github.com/damienheiser/home-assistant/blob/master/custom_components/rainforest/readme.md)

None
Authors: [@jrhorrisberger](https://github.com/jrhorrisberger), [@damienheiser](https://github.com/damienheiser).


#### [SamsungTV Smart v0.5.0](https://github.com/ollo69/ha-samsungtv-smart)


Authors: [@jaruba](https://github.com/jaruba), [@ollo69](https://github.com/ollo69), [@screwdgeh](https://github.com/screwdgeh).


#### [Scheduler integration v0.0.0](https://github.com/nielsfaber/scheduler-component)


Authors: [@nielsfaber](https://github.com/nielsfaber).


#### [SmartThinQ LGE Sensors v0.12.10](https://github.com/ollo69/ha-smartthinq-sensors)


Authors: [@ollo69](https://github.com/ollo69).


#### [SpaceX Launches and Starman v029](https://github.com/djtimca/haspacex)


Authors: [@djtimca](https://github.com/djtimca).


#### [Sun2 v2.0.3](https://github.com/pnbruckner/ha-sun2/blob/master/README.md)


Authors: [@pnbruckner](https://github.com/pnbruckner).


#### [UniFi Gateway v0.3.3](https://github.com/custom-components/sensor.unifigateway)


Authors: [@jchasey](https://github.com/jchasey).


#### [Watchman v0.5.0](https://github.com/dummylabs/thewatchman)

Home Assistant custom integration to keep track of missing entities and services in your config files
Authors: [@dummylabs](https://github.com/dummylabs).


#### [Weatheralerts v0.1.5](https://github.com/custom-components/weatheralerts)

A sensor that gives you weather alerts from alerts.weather.gov.
Authors: [@ludeeus](https://github.com/ludeeus), [@jlverhagen](https://github.com/jlverhagen).


#### [Wyze v0.1.7](https://github.com/JoshuaMulliken/ha-wyzeapi#readme)

Home Assistant Integration for Wyze devices.
Authors: [@JoshuaMulliken](https://github.com/JoshuaMulliken).
</details>

<details><summary>29 lovelace plugins</summary>

#### [Atomic Calendar Revive v6.2.0](https://github.com/totaldebug/atomic-calendar-revive)
Custom calendar card for Home Assistant with Lovelace


#### [Auto Entities v1.9.1](https://github.com/thomasloven/lovelace-auto-entities)
🔹Automatically populate the entities-list of lovelace cards


#### [Badge Card](https://github.com/thomasloven/lovelace-badge-card)
🔹 Place badges anywhere in the lovelace layout


#### [Button Card v3.4.2](https://github.com/custom-cards/button-card)
❇️ Lovelace button-card for home assistant


#### [Canary v0.3.4](https://github.com/jcwillox/lovelace-canary)
🐤 Adds many useful extensions to lovelace, such as templating secondary info, stacking within a card and more!


#### [Card Mod v3.1.2](https://github.com/thomasloven/lovelace-card-mod)
🔹 Add CSS styles to (almost) any lovelace card


#### [Card Tools v11](https://github.com/thomasloven/lovelace-card-tools)
🔹A collection of tools for other lovelace plugins to use


#### [Decluttering Card v0.6.3](https://github.com/custom-cards/decluttering-card)
🧹 Declutter your lovelace configuration with the help of this card


#### [Favicon Counter v1.0.0](https://github.com/custom-cards/favicon-counter)
Show a notification count badge.


#### [Fold Entity Row v20.0.12](https://github.com/thomasloven/lovelace-fold-entity-row)
🔹 A foldable row for entities card, containing other rows


#### [Frigate Card v2.1.0](https://github.com/dermotduffy/frigate-hass-card)
A Lovelace card for Frigate in Home Assistant


#### [Ha (Lovelace) Card Weather Conditions v1.9.12](https://github.com/r-renato/ha-card-weather-conditions)
Weather condition card (Lovelace) for Home Assistant.


#### [Kiosk Mode v1.7.2](https://github.com/maykar/kiosk-mode)
🙈 Hides the Home Assistant header and/or sidebar


#### [Layout Card v2.3.1](https://github.com/thomasloven/lovelace-layout-card)
🔹 Get more control over the placement of lovelace cards.


#### [Lovelace Home Feed Card v0.6.3](https://github.com/gadgetchnnel/lovelace-home-feed-card)
A custom Lovelace card for displaying a combination of persistent notifications, calendar events, and entities in the style of a feed.


#### [Lovelace Text Input Row v0.0.8](https://github.com/gadgetchnnel/lovelace-text-input-row)
A custom Lovelace text input row for use in entities cards


#### [Mini Graph Card v0.11.0](https://github.com/kalkih/mini-graph-card)
Minimalistic graph card for Home Assistant Lovelace UI


#### [Multiple Entity Row v4.4.1](https://github.com/benct/lovelace-multiple-entity-row)
Show multiple entity states and attributes on entity rows in Home Assistant's Lovelace UI


#### [My Cards Bundle](https://github.com/AnthonMS/my-cards)
Bundle of my custom Lovalace cards for Home Assistant. Includes: my-slider


#### [Power Wheel Card v0.1.5](https://github.com/gurbyz/power-wheel-card)
An intuitive way to represent the power and energy that your home is consuming or producing. (A custom card for the Lovelace UI of Home Assistant.)


#### [Restriction Card v1.2.7](https://github.com/iantrich/restriction-card)
🔒 Apply restrictions to Lovelace cards


#### [Scheduler Card v2.3.3](https://github.com/nielsfaber/scheduler-card)
HA Lovelace card for control of scheduler entities


#### [Simple Thermostat v2.4.3](https://github.com/nervetattoo/simple-thermostat)
A different take on the thermostat card for Home Assistant ♨️


#### [Slider Entity Row v17.2.1](https://github.com/thomasloven/lovelace-slider-entity-row)
🔹 Add sliders to entity cards


#### [Stack In Card v0.2.0](https://github.com/custom-cards/stack-in-card)
🛠 group multiple cards into one card without the borders


#### [State Switch v1.9.3](https://github.com/thomasloven/lovelace-state-switch)
🔹Dynamically replace lovelace cards depending on occasion


#### [Swipe Card v4.0.0](https://github.com/bramkragten/swipe-card)
Card that allows you to swipe throught multiple cards for Home Assistant Lovelace


#### [Timer Bar Card v1.16](https://github.com/rianadon/timer-bar-card)
A progress bar display for Home Assistant timers


#### [Weather Card v1.5.0](https://github.com/bramkragten/weather-card)
Weather Card with animated icons for Home Assistant Lovelace

</details>

<details><summary>7 addons</summary>

#### ESPHome v2022.2.5
ESPHome add-on for intelligently managing all your ESP8266/ESP32 devices


#### File editor v5.3.3
Simple browser-based file editor for Home Assistant


#### HA Scheduler v0.17
Home Assistant scheduler


#### Home Assistant Google Drive Backup v0.105.2
Automatically manage backups between Home Assistant and Google Drive


#### Portainer v2.0.0
Manage your Docker environment with ease


#### Samba share v9.5.1
Expose Home Assistant folders with SMB/CIFS


#### SDR to Home Assistant v0.1.11b
SDR/RTL Sensors to Home Assistant via MQTT with Autodiscovery

</details>
---

## Inspiration
The following are just some of the people that have inspired my smart home.

### Carlo
I aspire to Carlo's level of home connectedness. I have taken baby steps to giving my home a voice, but my speech routines are not being utilized quite as elegantly as at Carlo's house!
* Github: [Bear stone smart home configuration][carlo-github]
* Blog: [vCloudInfo][carlo-blog]
* YouTube: [vCloudInfo Channel][carlo-youtube]

### DrZzs
I wish I could be more like this guy. He is just so darn positive and happy all of the time. He taught me how to "Tasmota". I like to have one of his videos or streams playing in the background while I am coding.
* Github:  [SniperCanie's repositories][drzzs-github]
* YouTube: [DrZzs channel][drzzs-youtube]

### Frenck
I just learned of Frenck recently, but he is a long time member of the community. I just refactored my code to be similar to his config ([as discussed in this video][frenck-youtube-config]).
* Github: [Frenck's Home Assistant configuration][frenck-github]
* YouTube: [Frenck's channel][frenck-youtube]

---

All of my configuration files are tested against the most stable version of home-assistant using [Github Actions](https://github.com/brianhanifin/Home-Assistant-Config/actions).


[bedroom_switches]: ./README-images/xiaomi_double_switch.jpeg

[esphome-config]: https://github.com/brianhanifin/esphome-config

[ha-version]: https://www.home-assistant.io/blog/categories/release-notes/
[ha-version-shield]: https://img.shields.io/badge/2022.3.0b5-333333?logo=home%20assistant

[github-build-status-shield]: https://github.com/brianhanifin/Home-Assistant-Config/actions/workflows/build.yml/badge.svg
[github-build-status]: https://github.com/brianhanifin/Home-Assistant-Config/actions/workflows/build.yml
[github-linter-status-shield]: https://github.com/brianhanifin/Home-Assistant-Config/actions/workflows/linters.yml/badge.svg
[github-linter-status]: https://github.com/brianhanifin/Home-Assistant-Config/actions/workflows/linters.yml

[commits-shield]: https://img.shields.io/github/commit-activity/m/brianhanifin/Home-Assistant-Config.svg?logo=github&logoColor=838B95
[commits]: https://github.com/brianhanifin/Home-Assistant-Config/pulse

[code-lines-shield]: https://img.shields.io/badge/lines%20of%20code-48619-informational
[code-link]: https://github.com/brianhanifin/Home-Assistant-Config/pulse

[maintained]: https://img.shields.io/maintenance/yes/2022.svg

[github-last-commit]: https://img.shields.io/github/last-commit/BrianHanifin/Home-Assistant-Config.svg?logo=github&logoColor=838B95
[github-master]: https://github.com/BrianHanifin/Home-Assistant-Config/commits/master

[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?logo=discord&color=7289da
[discord]: https://discord.gg/c5DvZ4e

[discourse-shield]: https://img.shields.io/discourse/topics?color=46B4ED&label=community&logo=discourse&logoColor=46B4ED&server=https%3A%2F%2Fcommunity.home-assistant.io
[discourse]: https://community.home-assistant.io/u/brianhanifin/summary

[esphome-ble-hub]:https://esphome.io/components/esp32_ble_tracker.html
[esphome-sonoff-basic]:https://esphome.io/devices/sonoff_basic.html

[hue-strip-guide]:https://char.gd/blog/2018/building-better-cheaper-philips-hue-led-strips

[carlo-blog]: https://www.vcloudinfo.com
[carlo-github]: https://github.com/CCOSTAN/Home-AssistantConfig
[carlo-youtube]: https://YouTube.com/vCloudInfo
[carlo-blog-smoke]: https://www.vcloudinfo.com/2017/06/psa-check-out-your-smoke-detectors-once.html

[drzzs-github]: https://github.com/Snipercaine
[drzzs-youtube]: https://www.youtube.com/channel/UC7G4tLa4Kt6A9e3hJ-HO8ng

[frenck-github]: https://github.com/frenck/home-assistant-config/
[frenck-youtube]: https://www.youtube.com/user/Frenck
[frenck-youtube-config]: https://youtu.be/lndeybw21PY