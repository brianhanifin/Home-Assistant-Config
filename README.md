# Hanifin Smart Home

| Repository Status | Home Assistant Community |
| :--- | :--- |
| [![Github Action Status][github-build-status-shield]][github-build-status] [![travis build status][travis-build-status-shield]][travis-build-status] [![last commit time][github-last-commit]][github-master] [![GitHub Activity][commits-shield]][commits] | [![Community Forum][forum-shield]][forum] [![Discord][discord-shield]][discord] |

## About our smart home
I started using Home Assistant in the spring of 2018 when I outgrew the limited automations on Apple's HomeKit platform. While my Home Assistant initially included many HomeKit smart plugs (mostly the iHome ones), I eventually moved away from Homekit altogether.

Home Assistant now manages our smart home devices with lots of intelligence handled by my automations. It is important that our devices can be controlled by standard wall switches where possible, but we use Alexa to control our devices with our voice. Not only can we talk to Alexa, but she can let us know when the laundry wash cycle is complete (thanks to the help of a power monitoring smart plug).

## User Interface
### Amazon Alexa
<span style="float:left">![amazon echo][amazon-echo]</span> Our primary way we interact with Alexa is via Echo devices in all of the major rooms of the house. Alexa makes announcments when something needs our immediate attention: such as when it is time to leave for school, or the dog's water bowl needs to be refilled.

### Physical Buttons
<span style="float:left">![medicine button][button-medicine]</span> Recently I stuck a wireless push button inside the cabinet where we keep our dog's seizure medicine. When we prepare his pill treats for the day, and give him his first dose a press of the button logs today's date. Around 9am an automation runs that announces that the dog's medicine needs his medicine. However, if the button was pressed earlier in the day the announcement is not made.

My wife is really happy with how this is working and I am considering incorporating more of these into our daily routine. Maybe Home Assistant could take over more of our household reminders from apps on our Phones?

### Lovelace

| | | | | |
| --- | --- | --- | --- | --- |
| [![home][lovelace-01t]][lovelace-01] | [![rooms][lovelace-02t]][lovelace-02] | [![outside][lovelace-03t]][lovelace-03] | [![wakeup][lovelace-04t]][lovelace-04] | [![tools][lovelace-05t]][lovelace-05] |

---

## Hardware

### ESPHome
I am inspired to finally find uses for the bag full of random ESP boards I purchased about a year ago, when I thought I was going to create my own sensors to work with Homebridge. *While waiting for them to arrive on a slow boat from China, I discovered Home Assistant and decided to go a different way!*
#### ESP32
**Bluetooth Low Energy Device Hub**:
[Using the example code from esphome.io][esphome-ble-hub] I deployed a bridge in my Garage to pass along the data from the Xiaomi MiFlora sensor I stuck in one of our plant pots in the Front Yard. I had this for over almost a year and was unable to get the data into Home Assistant, until now! :smile:
#### ESP8266 + ESP8285
-**Water Bowl Sensor**: [Using the Sonoff Basic button press binary sensor][esphome-sonoff-basic] as a starting point, I deployed a ESP8285 with two simple jumper wires attached to sense when the dog's water bowl becomes empty. If the sensor still reads the bowl as empty after 5 minutes then Alexa announces it is time to fill the bowl.-
#### SonOff Plugs
**Basic, S31, POW R2**:
These plugs control a hot water circulation pump, floor fans, landscape lighting, Christmas light strings, etc. One monitors the power usage of the Washing Machine so Alexa can announce when the clothes are ready to be moved to the dryer.

I replaced my HomeKit smart plugs with various SonOff plugs. First with Tasmota installed, then I replaced the Tasmota firmware with ESPHome firmware which loses the MQTT layer in favor of native Home Assistant integration (and I suspect speed).
#### Tuya Plugs
**Luntak and Zoozee Brand**:
I have 8 of these than I used Tuya-convert to replace the stock firmware with ESPHome firmware. I use these for various things like floor/tabletop fans, decorative yard lights, and the white noise sound machine in our bedroom.

### Harmony Ultimate Hub
We have become an almost controller-free house! Our two TV areas and both have hubs to manage switching inputs to all of the devices hooked up to them. The Harmony Alexa skill handles most of the voice commands, and setup Alexa Routines to handle the two commands that overlap on the two TVs.
* "Alexa, turn on the " *Family Room or Play Room* " Computer."
* "Alexa, turn on the " *Family Room or Play Room* " TV."
* "Alexa, turn off the " *Family Room or Play Room* " TV."

### Insteon
I started with HomeKit compatible *Insteon* lamp dimmer modules. I plug a few... er... lamps into them. :)

### Lutron
Along with Inteon dimmer modules I also started installing *Lutron* in-wall dimmer switches and in-wall wireless remotes. The remotes are installed in several locations that otherwise would not have a light switch. Somehow our Play Room never had a light switch installed, now it does.

### Philips Hue
Hue color bulbs for Porch Light, Garage Entry Light, and my Family Room Table Lamp. The Porch bulb changes color based on the current national holiday (or family birthday/anniversary) while the Garage Entry Light and Family Room Table Lamp flash briefly, then stay on to indicate certain events: such as the garage door is open, or Alexa is announcing it is time for the boys to go to bed. Two of my remaining five Hue bulbs are reserved for an additional two porch/entryway hanging lamps, so I can set 3 colors for each holiday! :)

### Philips Hue Compabile Light Strips
I followed [this guide][hue-strip-guide] to build an inexpensive color changing light strip that is installed under our kitchen cabinets. This light is motion controlled, so we can fill our cup with water at night. The light gets brighter when either of the kitchen lights are turned on, and dim again when they are off.

I plan to build one more strip to light the inside of our pantry. I will be using a wireless contact sensor to turn the lights on and off.

### Presence detection
I maintain a list of close and extended family member's phones to track using NMAP pings. Unfortunately, it appears some phones go to sleep for too long so it keeps thinking they leave and come back. My mother-in-law doesn't appreciate Alexa welcoming her home 4 times per hour. So I had to disable that feature for her phone.

Based on DrZzs recommendation I switch presence tracking for my and my wife's phones to Life360. This has made me comfortable enough to do things like having Home Assistant close the garage door if one of us leaves the home zone. This covers us for those few times we may forget to close the door before driving away! :)

### Smoke + Carbon Monoxide Detectors
Thanks to Carlo's article "[PSA: CHECK OUT YOUR SMOKE DETECTORS (ONCE EVERY 10 YEARS)][carlo-blog-smoke]" I realized that I have lived in my house for almost 11 years now, and we're due for new smoke detectors.

I have added 6 of these around the house and setup an iOS alert to alert my and my wife's phones should the Smoke or CO sensor be triggered anywhere in the house. As they are interconnected they all appear as one device in Wink and Home Assistant! :)

### Xiaomi
This Chinese company makes a lot of very useful and inexpensive wireless smart home products. I use their Zigbee smart hub to get these devices to talk to Home Assistant.
#### Contact Sensors
I use their door/window sensors to turn the light in the shoe closet on and off, and remind us when we leave the Glowforge vent window open.
#### Motion Sensors
Two motion sensors watch for people to enter the kitchen so they can turn on the undercabinet light strip.
#### Leak Sensors
As soon as we finished our Kitchen remodel I set one of these wireless little dics under the sink. Should water pool and activate the senor a Home Assistant "Watch Dog" will instantly have Alexa announce there is a water leak all over the house, and an alert will be sent to my phone!

I ordered a few more so I could have better leak coverage around the house, including the water heater tray. We had a water heater leak slowly over the summer and we didn't realize it until it got worse.

### Ubiquiti Unifi WiFi
Eventually you outgrow even the fanciest home WiFi setup. There were just too many devices for my Netgear Orbi mesh networking system to handle, so I had to upgrade to a business grade solution.

Pros:
* Rock solid WiFi all throughout the downstairs.
* Wife and kids don't complain about the WiFi anymore!
* Long Ethernet cable runs make all access points equally fast!

Cons:
* Requires a long Ethernet cable run to each Access Point. (But also a "Pro"... see the last point above.)


### Wink Hub
I picked up an inexpensive version 1 Wink Hub so I could add Z-Wave devices and replace my Lutron Hub. I have now added Kidee Smoke + Carbon Monoxide detectors as well.

### Z-Wave
I have added some GE Z-Wave in-wall switches in the kitchen since we don't care to dim the overhead lights in there. I also have a few dimmers as well.

---

## Inspiration
The following are just some of the people that have inspired my smart home.

### Carlo
I aspire to Carlo's level of home connectedness. I have taken baby steps to giving my home a voice, but my speech routines are not being utilized quite as elegantly as at Carlo's house!
* Github: [Bear Stone Smart Home Configuration][carlo-github]
* Blog: [vCloudInfo][carlo-blog]
* YouTube: [vCloudInfo Channel][carlo-youtube]

### DrZzs
I wish I could be more like this guy. He is just so darn positive and happy all of the time. He taught me how to "Tasmota". I like to have one of his videos or streams playing in the background while I am coding.
* Github:  [SniperCanie's Repositories][drzzs-github]
* YouTube: [DrZzs Channel][drzzs-youtube]

### Frenck
I just learned of Frenck recently, but he is a long time member of the community. I just refactored my code to be similar to his config ([as discussed in this video][frenck-youtube-config]).
* Github: [Frenck's Home Assistant Configuration][frenck-github]
* YouTube: [Frenck's Channel][frenck-youtube]

---

All of my configuration files are tested against the most stable version of home-assistant using [Travis][travis-build-status].


[lovelace-01t]: ./README-images/01_home_t.jpeg
[lovelace-02t]: ./README-images/02_rooms_t.jpeg
[lovelace-03t]: ./README-images/03_outside_t.jpeg
[lovelace-04t]: ./README-images/04_wakeup_t.jpeg
[lovelace-05t]: ./README-images/05_tools_t.jpeg

[lovelace-01]: ./README-images/01_home.jpeg
[lovelace-02]: ./README-images/02_rooms.jpeg
[lovelace-03]: ./README-images/03_outside.jpeg
[lovelace-04]: ./README-images/04_wakeup.jpeg
[lovelace-05]: ./README-images/05_tools.jpeg

[amazon-echo]: ./README-images/echo.jpeg
[button-medicine]: ./README-images/button_medicine.jpeg

[commits-shield]: https://img.shields.io/github/commit-activity/m/brianhanifin/Home-Assistant-Config.svg
[commits]: https://github.com/brianhanifin/Home-Assistant-Config/commits/master
[github-last-commit]: https://img.shields.io/github/last-commit/BrianHanifin/Home-Assistant-Config.svg?style=plasticr
[github-master]: https://github.com/BrianHanifin/Home-Assistant-Config/commits/master

[github-build-status]: https://github.com/brianhanifin/Home-Assistant-Config/actions?workflow=build
[github-build-status-shield]: https://github.com/brianhanifin/Home-Assistant-Config/workflows/build/badge.svg

[travis-build-status]: https://travis-ci.org/brianhanifin/Home-Assistant-Config
[travis-build-status-shield]: https://travis-ci.org/brianhanifin/Home-Assistant-Config.svg?branch=master

[uptime-status-shield]: https://img.shields.io/uptimerobot/status/m781778026-6d060136ab5e0b0b72139815.svg
[uptime-robot]: https://uptimerobot.com/dashboard.php#tvMode

[discord-shield]: https://img.shields.io/discord/330944238910963714.svg
[discord]: https://discord.gg/c5DvZ4e

[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg
[forum]: https://community.home-assistant.io/u/brianhanifin/summary


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
