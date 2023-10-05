# Repository status

[![Home Assistant version][ha-version-shield]][ha-version] [![Github action status][github-build-status-shield]][github-build-status] [![Github linter status][github-linter-status-shield]][github-linter-status]

[![Last commit][github-last-commit]][github-master] [![GitHub activity][commits-shield]][commits]

# Repository statistics
| Lines of code | Entities | Devices | Areas | Domains | Automations | Scripts |
| :--: | :--: | :--: | :--: | :--: | :--: |
| **38,418** | 1,495 | 286 | 15 | 108 | 63 |

# Index

* [Smart home articles](#smart-home-articles)
* [Summary of our smart home](#summary-of-our-smart-home)
* [How we control our smart home](#how-we-control-our-smart-home)
  - [Physical control](#physical-control)
    + [In-wall dimmers and switches](#in-wall-dimmers-and-switches)
    + [Bedside toggle switches](#bedside-toggle-switches)
  - [Voice control](#voice-control)
  - [Screen control](#screen-control)
    + [Mobile dashboard](#mobile-dashboard)
    + [Cast dashboard](#cast-dashboard)
* [Smart home devices](#smart-home-devices)
  - [Inovelli red series switches and dimmers](#inovelli-red-series-switches-and-dimmers)
    + [Project ideas](#project-ideas)
  - [Lutron caseta](#lutron-caseta)
    + [Project ideas](#project-ideas-1)
  - [Philips hue bulbs](#philips-hue-bulbs)
    + [Project ideas](#project-ideas-2)
  - [Smoke + carbon monoxide detectors](#smoke--carbon-monoxide-detectors)
    + [Project ideas](#project-ideas-3)
  - [Aqara sensors & buttons](#aqara-sensors--buttons)
    + [Project ideas](#project-ideas-4)
  - [DIY smart home devices](#diy-smart-home-devices)
    + [Project ideas](#project-ideas-5)
  - [SONOFF S31 plugs](#sonoff-s31-plugs)
    + [Power monitoring project ideas](#power-monitoring-project-ideas)
    + [S31 lite project ideas](#s31-lite-project-ideas)
  - [Presence detection](#presence-detection)
      + [Life360 integration](#life360-integration)
      + [UniFi integration](#unifi-integration)
      + [Guest mode helper](#guest-mode-helper)
* [Wireless communications](#wireless-communications)
  - [Bluetooth](#bluetooth)
  - [Software defined radio](#software-defined-radio)
  - [Wi-fi: Ubiquiti Unifi](#wi-fi-ubiquiti-unifi)
  - [Zigbee](#zigbee)
  - [Z-wave](#z-wave)
* [Technical details](#technical-details)
* [Home Assistant community](#home-assistant-community)

# Smart home articles

I write instructional articles on [brianhanifin.com](https://brianhanifin.com/). Topics primarily revolve around Home Assistant and ESPHome code and devices, but I also I have written about my HomeLab server setup.

# Summary of our smart home
I started using Home Assistant in the spring of 2018 when we outgrew the limited automations on Apple's HomeKit platform. Our Home Assistant initially included many HomeKit smart plugs our collection of smart lights, switches, plugs, cameras, and sensors. Since we have added many devices that use protocols like Zigbee and Z-Wave and even several custom built electronic modules.

Home Assistant now manages our smart home devices with lots of intelligence handled by automations. It is important that our devices can be controlled by standard wall switches, but we also use Google Nest speakers to control our devices with our voice. Not only can we talk to Google, but she can let us know when a laundry cycle, 3D Print, or laser cutting job is complete.

# How we control our smart home

## Physical control
We use a variety of physical switches from hard-wired to battery powered.

### In-wall dimmers and switches
These can be used to control dumb lights. However, some devices allow you pass constant power so you can control smart bulbs with Home Assistant. For example a switch in my Dining Room leaves power to my Hue bulbs so I can turn the lights on with my voice or the physical wall switch.

<span style="float:left">![bedroom_switches]</span>
### Bedside toggle switches
Battery powered devices with 6 buttons on each bedside table. Top row: single clicks toggle lights on either side of the bed, while a double clicks toggle a third lamp. Second row: single click toggles the fan or sound machine. Bottom row: single clicks to the left button toggles the window air conditioner between Cool and Fan only modes while the right button turns the Air Conditioner off.

## Voice control
We can also interact with our devices with Google Nest speakers and displays in all of the major rooms of the house.

Our Google Nest also make announcements when something needs our immediate attention. For example: when it is time to leave for school, or for the boys to turn their computers off before the Internet is turned off at bedtime.

## Screen control

<span style="float:right">[![mobile-ui]][mobile-ui-full]</span>
### Mobile dashboard
I interact with the Home Assistant app on my phone to check in on the status of devices and automations.

### Cast dashboard
* **Cameras**: when the doorbell is pressed our outdoor cameras get cast to the Google displays.
* **Countdown timers**: occasionally the wrong Google device starts a kitchen timer. To help with this issue Home Assistant casts a countdown timer status screen to the kitchen display while any timers are active.

# Smart home devices

> Disclosure: This section contains affiliate links. If you decide to make a purchase, I'll make a small commission at no extra cost to you.

## Inovelli red series switches and dimmers
Device recommendations: [Red series dimmer](https://amzn.to/2ZY73i3), [Red series switch](https://amzn.to/3r2WtT5), [Red series fan & light switch](https://amzn.to/3q0yB12)

Inovelli z-wave devices are high quality and they really care about our niche community. The red series switches handle double, triple, quadruple, and event quintuple click events. These even have a led light strip on the right side which we use different color and animations to indicate the state of things around the house.

### Project ideas
1. **Multi-click actions!** 2x click to turn on/off the bright floor lamp, 3x click to turn on/off the floor fan, 4x click to activate your "good night" scene, 5x click to activate guest mode on your way to answer the door!<br>
*See my automation: [automations/buttons/zwjs_button_click.yaml](https://github.com/brianhanifin/Home-Assistant-Config/blob/master/automations/buttons/zwjs_button_click.yaml)*
2. **House status indicator** Use the LED strip to indicate when the garage is open, or the alarm is disarmed.<br>
*See my article: "[Inovelli red series status LED update](https://brianhanifin.com/posts/inovelli-red-series-status-led-update/)"*

## Lutron caseta
Device recommendations: [dimmer](https://amzn.to/3pHXJth), [pico remote](https://amzn.to/2OYVHZ4), [dimmer and pico remote](https://amzn.to/3unpD0Y), [Lutron caseta pro bridge](https://amzn.to/3aH1pqO)

In-wall dimmer switches and in-wall (or handheld) wireless remotes. Get the [Lutron caseta pro bridge](https://amzn.to/3aH1pqO) so you can use your pico remotes with Home Assistant to control any device in your house! The standard bridge is less expensive but you cannot watch for pico remote button press events.

### Project ideas
1. Add a battery powered pico remote next to a room which doesn't have a wall switch! Control a smart bulb by any manufacturer! Our Play room was lacking a switch, so I screwed the mount to the drywall and covered with with a standard cover! :beers:
2. Replace a dumb wired light switch or dimmer with a caseta dimmer so Home Assistant can automatically turn the lights on at night when a motion sensor detects you have entered the room!
3. Use Home Assistant to brighten the lights gradually to help you wake up in the morning.

## Philips hue bulbs
Device recommendations: [starter Kit](https://amzn.to/37AqeTq) (3 color bulbs, dimmer, & hub)

The Hue ecosystem is easy to get setup with Home Assistant. We primarily use their tunable white bulbs for plug in floor and table lamps, but we do have 9 colored bulbs in our dining room chandelier for holiday fun.

### Project ideas
1. Use these bulbs to make your plug in lamps controllable by Home Assistant.
2. Create a realistic sunrise to wakeup in the morning using the tunable white light.

## Smoke + carbon monoxide detectors

Device recommendation: [first alert z-wave 2-in-1 smoke detector & carbon monoxide alarm](https://amzn.to/3r0RjGV)

Thanks to Carlo's article "[PSA: CHECK OUT YOUR SMOKE DETECTORS (ONCE EVERY 10 YEARS)][carlo-blog-smoke]" I realized that I had lived in my house for almost 11 years, and we were due for new smoke detectors. So I replaced them with new First Alert zcombo z-wave smoke detectors.

### Project ideas:
1. **Safety alert!** Have Home Assistant alert you which detector sensed the smoke so you can decide whether to try to put it out, or get to safety!

## Aqara sensors & buttons
Device recommendations: [wireless buttons](https://amzn.to/3q4jd3w), [motion & luminance sensors](https://amzn.to/3q0OOTK), [temperature & humidity sensors](https://amzn.to/2ZYWV8I), [door & window sensors](https://amzn.to/2ZWptjl), [leak sensors](https://amzn.to/3r1bYef), [vibration sensors](https://amzn.to/2ZUvrBl)
Hub recomendations: [Phoscon conbee II USB gateway](https://amzn.to/2Mz3jk8), [Aqara homekit hub](https://amzn.to/37TN6xv), [Aqara starter kit: hub, plug, button, motion, door/window](https://amzn.to/2O6STIO)

This chinese company makes a lot of very useful and inexpensive wireless smart home products. At first I used their Zigbee smart hub to get these devices to talk to Home Assistant. However I now use a USB stick connected to my server to communicate with all of my Zigbee devices.

### Project ideas
1. **Flood damage alert!** _This has saved us from major damage once and minor under the sink leak damage twice!_ Place leak sensors under your all sinks, dishwasher, clothes washer, refrigerator, and water heater. Setup an alert to notify you where the leak is. This will give you valuable time to stop major flood damage!
2. **Door and window sensors**: Stick door and window sensors on doors and windows around your house and have Home Assistant remind you to close the doors and windows when it starts to get warm outside.
3. **Motion lights**: stick a motion sensor in your<br>
  3a. Kitchen to turn on an LED strip under your cabinets to give yourself a nightlight when getting water in the middle of the night.<br>
  3b. Bedroom to light a dim path to the bathroom.
4. **Medicine logger**: stick a wireless button inside the medicine cabinet to log when you gave seizure medicine to your dog.
5. **Automatic bathroom exhaust**: use a temperature & humidity sensor to automatically turn on your exhaust fan and turn it back off when the humidity drops again.

# DIY smart home devices

I have flashed the below devices with ESPHome firmware which I have full control
over! You can see my code at my [esphome-config GitHub repository][esphome-config].

## Shelly 1 boards
Device recommendations: shelly 1 ([1 pack](https://amzn.to/3qKTyhI), [2 pack](https://amzn.to/3bw9bmN)), [shelly 2](https://amzn.to/37Aq7qY)

These devices are great for shoving in a box behind a light switch to add smarts.

### Project ideas
1. **Hue bulb functional light switch**: my dining room has a 9 bulb chandelier, this provides constant power, while allowing the switch to remain functional.
2. **Smart bathroom exhaust fan**<br>
*2a.* turns the fan off after 10 minutes when manually turned on (*note: a battery powered motion sensor resets the countdown*).<br>
*2b.* turns the fan on then back off when the humidity is up due to a shower (*note: a battery powered humidity sensor in the bathroom is compared to one in a neighboring room*).
3. **Garage door controller**: I plan to replace the cloud based chamberlain MyQ controller soon using [the hook up's video for reference ](https://www.youtube.com/watch?v=WEZUxXNiERQ).

## SONOFF S31 plugs
Device recommendations: [S31](https://amzn.to/2OOEilB), [S31 lite](https://amzn.to/3xibdmw)

The SONOFF S31 is a reliable wi-fi controlled smart switch which can be flashed with Tasmota or ESPHome if you wish. The original S31 has power monitoring built in, while the new S31 lite omits that for a discount.

### Power monitoring project ideas
*Note: the relay can be left always on to put these in a monitor only mode.*
1. Monitor your washing machine so Home Assistant can notify you when your wash is ready to be hung up or moved to the dryer! No more stinky clothes!
2. Monitor your dishwasher or clothes dryer.
3. Monitor your 3D Printer or Laser Cutter to let you know when it is time to check out that thing you just created!

### S31 lite project ideas
1. Plug one of these into every floor and table fan you own and just ask your Google or Alexa to *"turn on the bedroom fan!"*.
2. Plug one into a sound machine to help you sleep at night. Have Home Assistant automatically start this when your phone starts charging for the night.

## Presence detection

### Life360 integration
I use [Life360](https://www.life360.com/) for presence tracking on my son's, wife's, and my phone. This has made me comfortable enough to do things like having Home Assistant close the garage door if one of us leaves the home zone. This covers us for those few times we may forget to close the door before driving away! :)

### UniFi integration
For extended family visitors I use the [Home Assistant Ubiquiti UniFi integration](https://www.home-assistant.io/integrations/unifi/#presence-detection) to track when their phones are connected to my wireless access points.

### Guest mode helper
Finally, I have a "Guest Mode" input_boolean setup as both a trigger and a condition on many of my lighting and front door locking automations.

# Wireless communications

## Bluetooth
Recommendations: [Long Range USB Bluetooth Adapter](https://amzn.to/3fJ05Jg), [ESP32 boards](https://amzn.to/3WFLdfq), [Switchbox Button Pusher](https://amzn.to/3DU0wc2), [Xiaomi Mijia Thermometer 2](https://www.aliexpress.us/item/3256801169431856.html)

Home Assistant 2022.10 gave us full control of Bluetooth devices. You can even use [Bluetooth Proxies][bluetooth-proxies] to
extend your bluetooth control range.

## Homekit
Home assistant supports Homekit natively which opens up many quality devices that would not otherwise be
available to us. Homekit also allows me to bypass [Ecobee Thermostat](https://amzn.to/3WFxHZh)'s cloud services and control my thermostat locally!

Pros:
  * **Local control** of every device through Home Assistant (no Apple devices needed)!
  * Additional quality devices.

Cons:
  * Devices can be more costly.

## Software defined radio
Recommendations: [NooElec NESDR Mini 2 SDR](https://amzn.to/3zXc90C), [AcuRite Outdoor Thermometer](https://amzn.to/3fKngmx), [AcuRite Fridge and Freezer Thermometer](https://amzn.to/3FRYMCA)

## Wi-fi: Ubiquiti Unifi
Recommendations: [Unifi 6 lite access point](https://amzn.to/3q1OUut) (wi-fi 6), [Unifi AC-PRO access point](https://amzn.to/2NMc1vW) (802.11ac, one upstairs and one at the back of the house), [Unifi security gateway](https://amzn.to/2NEbooj)

Eventually you outgrow even the fanciest home wi-fi setup. There were just too many devices for my Netgear orbi mesh networking system to handle, so I had to upgrade to a business grade solution.

Pros:
* Rock solid wi-fi all throughout the house.
* Household members don't complain about the wi-fi anymore!
* Long ethernet cable runs make all access points equally fast!

Cons:
* Requires a long ethernet cable run to each access point. (But also a "pro"... see the last point above.)

## Zigbee
Recommendation: [Phoscon conbee II USB gateway](https://amzn.to/2Mz3jk8), Aqara Devices: [Leak Sensor](https://amzn.to/3tb8p7W), [Temperature Sensor](https://amzn.to/3ThmefJ), [Door/Window Sensor](https://amzn.to/3G3X4xQ), [Motion Sensor](https://amzn.to/3E8CxqK), [Plug with Energy Monitoring](https://amzn.to/3fNLtsk), [Push Button Remote](https://amzn.to/3TgeTwO)

[Zigbee2MQTT][zigbee2mqtt] now runs all of my zigbee devices. This includes the new [Inovelli Blue Switch][inovelli-blue-switch],
all of my philips hue bulbs, and lots of Aqara sensors!

## Z-wave
Recommendation: [Aeotec Z-Stick Gen5 Plus](https://amzn.to/3kw7YzO)

As of February 2021 Home Assistant's Z-Wave JS integration directly runs all of my z-wave devices.
To be precise I am running [Zwavejs2Mqtt][zwavejs2mqtt]] with MQTT disabled so I can make use of the
z-wave device management UI built in. This includes several in-wall switches and dimmers,
smoke detectors, and a bulb.

# Technical details

Our Home Assistant install has **286** devices
featuring **1,495** entities,
including **694** sensors. My YAML
files contain 38,418 lines of code.
All of my configuration files are tested against the most stable version of home-assistant using [Github Actions][github-actions].<details><summary>23 Custom integrations</summary>

## [Adaptive Lighting v1.19.0](https://github.com/basnijholt/adaptive-lighting#readme)
Adaptive Lighting custom component for Home AssistantAuthors:[@basnijholt](https://github.com/basnijholt), [@RubenKelevra](https://github.com/RubenKelevra), [@th3w1zard1](https://github.com/th3w1zard1), [@protyposis](https://github.com/protyposis).

## [Anniversaries v5.2.0](https://github.com/pinkywafer/Anniversaries)
Anniversary Countdown Sensor for Home AssistantAuthors:[@pinkywafer](https://github.com/pinkywafer).

## [Browser mod v2.3.0](https://github.com/thomasloven/hass-browser_mod/blob/master/README.md)


## [Eight Sleep Climate v2.0.0](https://github.com/amosyuen/ha-eight-sleep-climate)
Climate entity for controlling eight sleep bedAuthors:[@amosyuen](https://github.com/amosyuen).

## [Fontawesome icons v2.1.5](https://github.com/thomasloven/hass-fontawesome)


## [Frigate v5.0.0-beta.2](https://github.com/blakeblackshear/frigate)
Frigate integration for Home AssistantAuthors:[@blakeblackshear](https://github.com/blakeblackshear).

## [GE Home (SmartHQ) v0.6.8](https://github.com/simbaja/ha_gehome)
Authors:[@simbaja](https://github.com/simbaja).

## [Generate readme v0.5.0](https://github.com/custom-components/readme)
Authors:[@ludeeus](https://github.com/ludeeus).

## [Google Home v1.10.0](https://github.com/leikoilja/ha-google-home)
Home Assistant Google Home custom componentAuthors:[@leikoilja](https://github.com/leikoilja), [@DurgNomis-drol](https://github.com/DurgNomis-drol), [@ArnyminerZ](https://github.com/ArnyminerZ), [@KapJI](https://github.com/KapJI).

## [Home Assistant Community Store (HACS) v1.33.0](https://hacs.xyz/docs/configuration/start)
HACS gives you a powerful UI to handle downloads of all your custom needs.Authors:[@ludeeus](https://github.com/ludeeus).

## [Holidays v1.9.6](https://github.com/bruxy70/Holidays/)
📅 Custom Home Assistant integration for public holidays - also used for garbage_collection integration to automatically move scheduled events that fall on a public holiday (by an automation blueprint)Authors:[@bruxy70](https://github.com/bruxy70).

## [LocalTuya integration v5.2.1](https://github.com/rospogrigio/localtuya/)
Authors:[@rospogrigio](https://github.com/rospogrigio), [@postlund](https://github.com/postlund).

## [Lovelace Notify v1.0.0]()
Lovelace notification / alert component for Home AssistantAuthors:[@rr326](https://github.com/rr326).

## [NWS Alerts v4.1](https://github.com/finity69x2/nws_alerts/)
Authors:[@finity69x2](https://github.com/finity69x2).

## [Rainforest EMU-2 v1.3.2](https://github.com/ryanwinter/hass-rainforest-emu-2)
Authors:[@ryanwinter](https://github.com/ryanwinter).

## [SamsungTV Smart v0.12.0](https://github.com/ollo69/ha-samsungtv-smart)
Authors:[@jaruba](https://github.com/jaruba), [@ollo69](https://github.com/ollo69), [@screwdgeh](https://github.com/screwdgeh).

## [Simple Wyze Vacuum v1.8.9](https://github.com/romedtino/simple-wyze-vac)
Home Assistant Custom Component for Wyze VacuumAuthors:[romedtino](https://github.com/romedtino).

## [SmartThinQ LGE Sensors v0.33.3](https://github.com/ollo69/ha-smartthinq-sensors)
Authors:[@ollo69](https://github.com/ollo69).

## [Sun2 v2.4.0](https://github.com/pnbruckner/ha-sun2/blob/master/README.md)
Home Assistant Sun2 SensorAuthors:[@pnbruckner](https://github.com/pnbruckner).

## [UniFi Gateway v0.3.3](https://github.com/custom-components/sensor.unifigateway)
Authors:[@jchasey](https://github.com/jchasey).

## [Waste Management v0.1.6](https://github.com/dcmeglio/homeassistant-waste_management/blob/master/README.md)
Determines your next Waste Management (https://www.wm.com) pickup times for use in Home Assistant.Authors:[@dcmeglio](https://github.com/dcmeglio).

## [Watchman v0.5.1](https://github.com/dummylabs/thewatchman)
Home Assistant custom integration to keep track of missing entities and services in your config filesAuthors:[@dummylabs](https://github.com/dummylabs).

## [Wyze v0.1.22](https://github.com/SecKatie/ha-wyzeapi#readme)
Home Assistant Integration for Wyze devices.Authors:[@SecKatie](https://github.com/SecKatie).</details>

<details><summary>30 lovelace plugins</summary>

## [Apexcharts Card v2.0.4](https://github.com/RomRider/apexcharts-card)
📈 A Lovelace card to display advanced graphs and charts based on ApexChartsJS for Home Assistant

## [Atomic Calendar Revive v9.0.0](https://github.com/totaldebug/atomic-calendar-revive)
An advanced calendar card for Home Assistant Lovelace.

## [Auto Entities v1.12.1](https://github.com/thomasloven/lovelace-auto-entities)
🔹Automatically populate the entities-list of lovelace cards

## [Bubble Card v0.0.1-beta.8](https://github.com/Clooos/Bubble-Card)
Bubble Card is a minimalist card collection for Home Assistant with a nice pop-up touch.

## [Canary v0.4.0](https://github.com/jcwillox/lovelace-canary)
🐤 Adds many useful extensions to lovelace, such as templating secondary info, stacking within a card and more!

## [Card Mod v3.2.3](https://github.com/thomasloven/lovelace-card-mod)
🔹 Add CSS styles to (almost) any lovelace card

## [Card Tools v11](https://github.com/thomasloven/lovelace-card-tools)
🔹A collection of tools for other lovelace plugins to use

## [Clock Weather Card v1.1.0](https://github.com/pkissling/clock-weather-card)
A Home Assistant Card indicating today's date/time, along with an iOS inspired weather forecast for the next days with animated icons

## [Decluttering Card v1.0.0](https://github.com/custom-cards/decluttering-card)
🧹 Declutter your lovelace configuration with the help of this card

## [Flipdown Timer Card v0.4](https://github.com/pmongloid/flipdown-timer-card)
Flipdown Timer Card for Home Assistant Lovelace

## [Fold Entity Row v2.2.0](https://github.com/thomasloven/lovelace-fold-entity-row)
🔹 A foldable row for entities card, containing other rows

## [Frigate Card v5.2.0](https://github.com/dermotduffy/frigate-hass-card)
A Lovelace card for Frigate in Home Assistant

## [Kiosk Mode v4.1.0](https://github.com/NemesisRE/kiosk-mode)
🙈 Hides the Home Assistant header and/or sidebar

## [Layout Card v2.4.4](https://github.com/thomasloven/lovelace-layout-card)
🔹 Get more control over the placement of lovelace cards.

## [Lovelace Home Feed Card v0.6.4](https://github.com/gadgetchnnel/lovelace-home-feed-card)
A custom Lovelace card for displaying a combination of persistent notifications, calendar events, and entities in the style of a feed.

## [Mini Graph Card v0.11.0](https://github.com/kalkih/mini-graph-card)
Minimalistic graph card for Home Assistant Lovelace UI

## [More Info Card](https://github.com/thomasloven/lovelace-more-info-card)
🔹 Display the more-info dialog of any entity as a lovelace card

## [Multiple Entity Row v4.5.0](https://github.com/benct/lovelace-multiple-entity-row)
Show multiple entity states and attributes on entity rows in Home Assistant's Lovelace UI

## [Mushroom v3.1.0](https://github.com/piitaya/lovelace-mushroom)
Mushroom Cards - Build a beautiful dashboard easily 🍄

## [Number Box v4.14](https://github.com/htmltiger/numberbox-card)
Replace input_number sliders with plus and minus buttons

## [Power Wheel Card v0.1.5](https://github.com/gurbyz/power-wheel-card)
An intuitive way to represent the power and energy that your home is consuming or producing. (A custom card for the Lovelace UI of Home Assistant.)

## [Restriction Card v1.2.9](https://github.com/iantrich/restriction-card)
🔒 Apply restrictions to Lovelace cards

## [Simple Thermostat v2.5.0](https://github.com/nervetattoo/simple-thermostat)
A different take on the thermostat card for Home Assistant ♨️

## [State Switch v1.9.5](https://github.com/thomasloven/lovelace-state-switch)
🔹Dynamically replace lovelace cards depending on occasion

## [Swipe Card v5.0.0](https://github.com/bramkragten/swipe-card)
Card that allows you to swipe throught multiple cards for Home Assistant Lovelace

## [Tabbed Card v0.3.2](https://github.com/kinghat/tabbed-card)
a custom card for home assistant that utilizes tabs to segregate individual cards.

## [Timer Bar Card v1.29.1](https://github.com/rianadon/timer-bar-card)
A progress bar display for Home Assistant timers

## [Vacuum Card v2.7.6](https://github.com/denysdovhan/vacuum-card)
Vacuum cleaner card for Home Assistant Lovelace UI

## [Weather Card v1.5.0](https://github.com/bramkragten/weather-card)
Weather Card with animated icons for Home Assistant Lovelace

## [Weather Radar Card v2.1.0](https://github.com/Makin-Things/weather-radar-card)
A rain radar card using the tiled images from RainViewer
</details>


# Home Assistant community

[![Community Forum][discourse-shield]][discourse]
[![Discord][discord-shield]][discord]

The following are just some of the people that have inspired my smart home.

## Carlo
I aspire to Carlo's level of home connectedness. I have taken baby steps to giving my home a voice, but my speech routines are not being utilized quite as elegantly as at Carlo's house!
* Github: [Bear stone smart home configuration][carlo-github]
* Blog: [vCloudInfo][carlo-blog]
* YouTube: [vCloudInfo Channel][carlo-youtube]

## DrZzs
I wish I could be more like this guy. He is just so darn positive and happy all of the time. He taught me how to "Tasmota". I like to have one of his videos or streams playing in the background while I am coding.
* Github:  [SniperCanie's repositories][drzzs-github]
* YouTube: [DrZzs channel][drzzs-youtube]

## Frenck
I refactored my yaml files to be similar to his config ([as discussed in this video][frenck-youtube-config]).
* Github: [Frenck's Home Assistant configuration][frenck-github]
* YouTube: [Frenck's channel][frenck-youtube]

---

[mobile-ui]: ./README-images/mushroom_home_202206.jpg
[mobile-ui-full]: ./README-images/mushroom_home_202206_full.jpg
[bedroom_switches]: ./README-images/aqara-opple.jpg

[esphome-config]: https://github.com/brianhanifin/esphome-config

[ha-version]: https://www.home-assistant.io/blog/categories/release-notes/
[ha-version-shield]: https://img.shields.io/badge/2023.10.0-333333?logo=home%20assistant

[github-build-status-shield]: https://github.com/brianhanifin/Home-Assistant-Config/actions/workflows/build.yml/badge.svg
[github-build-status]: https://github.com/brianhanifin/Home-Assistant-Config/actions/workflows/build.yml
[github-linter-status-shield]: https://github.com/brianhanifin/Home-Assistant-Config/actions/workflows/linters.yml/badge.svg
[github-linter-status]: https://github.com/brianhanifin/Home-Assistant-Config/actions/workflows/linters.yml

[commits-shield]: https://img.shields.io/github/commit-activity/m/brianhanifin/Home-Assistant-Config.svg?logo=github&logoColor=838B95
[commits]: https://github.com/brianhanifin/Home-Assistant-Config/pulse

[code-lines-shield]: https://img.shields.io/badge/lines%20of%20code-38,418-informational
[code-link]: https://github.com/brianhanifin/Home-Assistant-Config/pulse

[maintained]: https://img.shields.io/maintenance/yes/2023.svg

[github-last-commit]: https://img.shields.io/github/last-commit/BrianHanifin/Home-Assistant-Config.svg?logo=github&logoColor=838B95
[github-master]: https://github.com/BrianHanifin/Home-Assistant-Config/commits/master

[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?logo=discord&color=7289da
[discord]: https://discord.gg/c5DvZ4e

[discourse-shield]: https://img.shields.io/discourse/topics?color=46B4ED&label=community&logo=discourse&logoColor=46B4ED&server=https%3A%2F%2Fcommunity.home-assistant.io
[discourse]: https://community.home-assistant.io/u/brianhanifin/summary

[bluetooth-proxies]: https://esphome.github.io/bluetooth-proxies/
[zigbee2mqtt]: https://www.zigbee2mqtt.io
[zwavejs2mqtt]: https://zwave-js.github.io/zwavejs2mqtt
[inovelli-blue-switch]: https://inovelli.com/products/blue-series-smart-2-1-switch-on-off-or-dimmer

[github-actions]: ./actions

[carlo-blog]: https://www.vcloudinfo.com
[carlo-github]: https://github.com/CCOSTAN/Home-AssistantConfig
[carlo-youtube]: https://YouTube.com/vCloudInfo
[carlo-blog-smoke]: https://www.vcloudinfo.com/2017/06/psa-check-out-your-smoke-detectors-once.html

[drzzs-github]: https://github.com/Snipercaine
[drzzs-youtube]: https://www.youtube.com/channel/UC7G4tLa4Kt6A9e3hJ-HO8ng

[frenck-github]: https://github.com/frenck/home-assistant-config/
[frenck-youtube]: https://www.youtube.com/user/Frenck
[frenck-youtube-config]: https://youtu.be/lndeybw21PY