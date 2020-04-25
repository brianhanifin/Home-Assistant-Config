# Hanifin Smart Home

| GitHub Repository | Home Assistant Community |
| :---| :--- |
| [![Github Action Status][github-build-status-shield]][github-build-status] [![last commit time][github-last-commit]][github-master] [![GitHub Activity][commits-shield]][commits]  | [![Community Forum][discourse-shield]][discourse] [![Discord][discord-shield]][discord] |

![ha-version-shield] ![maintained]

## About our smart home
I started using Home Assistant in the spring of 2018 when I outgrew the limited automations on Apple's HomeKit platform. While my Home Assistant initially included many HomeKit smart plugs (mostly the iHome ones), I eventually moved away from Homekit altogether.

Home Assistant now manages our smart home devices with lots of intelligence handled by my automations. It is important that our devices can be controlled by standard wall switches where possible, but we use Alexa to control our devices with our voice. Not only can we talk to Alexa, but she can let us know when the laundry wash cycle (or our Glowforge laser job) is complete, thanks to the help of a power monitoring smart plug.

As of my last commit I have **1057 entities**, with **327 sensors** in Home Assistant. I am also using **26 custom components**.

## User Interface
### Amazon Alexa
<span style="float:left">![amazon echo][amazon-echo]</span> Our primary way we interact with Alexa is via Echo devices in all of the major rooms of the house. Alexa makes announcments when something needs our immediate attention: such as when it is time to leave for school, or the dog's water bowl needs to be refilled.

### Physical Buttons

#### Dog Medicine Logger
<span style="float:left">![medicine button][button-medicine]</span> Recently I stuck a wireless push button inside the cabinet where we keep our dog's seizure medicine. When we prepare his pill treats for the day, and give him his first dose a press of the button logs today's date. Around 9am an automation runs that announces that the dog's medicine needs his medicine. However, if the button was pressed earlier in the day the announcement is not made.

My wife is really happy with how this is working and I am considering incorporating more of these into our daily routine. Maybe Home Assistant could take over more of our household reminders from apps on our Phones?

#### Bedside Toggle Switches
<span style="float:left">![bedroom_switches]</span>I added a battery powered Xiaomi double switch to my wife's bedside table. Single clicks toggle the lights on either side of our bed. While a long press toggles the bedroom fans, or the sound machine.

### Official User Interface (Lovelace)

[![home][lovelace-00t]][lovelace-00]

---

## Hardware

### ESPHome
I am inspired to finally find uses for the bag full of random ESP boards I purchased about a year ago, when I thought I was going to create my own sensors to work with Homebridge. *While waiting for them to arrive on a slow boat from China, I discovered Home Assistant and decided to go a different way!*

#### ESP32
**Bluetooth Low Energy Device Hub**:
[Using the example code from esphome.io][esphome-ble-hub] I deployed a bridge in my Garage to pass along the data from the Xiaomi MiFlora sensor I stuck in one of our plant pots in the Front Yard. I had this for over almost a year and was unable to get the data into Home Assistant, until now! :smile:

#### Shelly 1 Boards
These devices are great for shoving in a box behind a light switch to add smarts.

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

### Lutron
In-wall dimmer switches and in-wall wireless remotes. The remotes are installed in several locations that otherwise would not have a light switch. Somehow our Play Room never had a light switch installed, now it does.

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

I have begun replacing them with new First Alert ZCombo Z-Wave smoke dectors.

### Xiaomi
This Chinese company makes a lot of very useful and inexpensive wireless smart home products. I use their Zigbee smart hub to get these devices to talk to Home Assistant.
#### Buttons
I use a small battery powered button to track when the dog's medicine has been prepared for the day. Also, a double switch unit is on my wife's bedside table to sliently operate lights and devices in our room at night.
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

### Zigbee
I have all of my Philips Hue white bulbs run off of the Conbee II Zigbee USB stick, as well as a Xiaomi Humidity/Temperature sensor.

### Z-Wave
I have added some GE Z-Wave in-wall switches in the kitchen since we don't care to dim the overhead lights in there. I also have a few dimmers as well.

## Technical Details




### Custom Components

<dl>
  
  <dt> variable </dt>
  
  <dt> National Weather Service Radar </dt>
  
  <dt> Breaking Changes </dt>
  
  <dt> HACS (Home Assistant Community Store) </dt>
  
  <dd> Manage (Install, track, upgrade) and discover custom elements for Home Assistant. </dd>
  
  <dt> Logbook Cache </dt>
  
  <dt> Browser mod </dt>
  
  <dt> ics </dt>
  
  <dt> Weatheralerts </dt>
  
  <dt> Config Check </dt>
  
  <dt> Alexa Media Player </dt>
  
  <dt> Amcrest Camera </dt>
  
  <dt> Youtube Sensor </dt>
  
  <dt> UniFi Gateway </dt>
  
  <dt> Anniversaries </dt>
  
  <dt> Lovelace Gen </dt>
  
  <dt> Battery Level </dt>
  
  <dt> Illuminance </dt>
  
  <dt> UI Logs </dt>
  
  <dt> Lutron Caséta Smart Bridge PRO / RA2 Select </dt>
  
  <dt> Apple TV </dt>
  
  <dt> UI Logs </dt>
  
  <dt> Generate readme </dt>
  
  <dd> Generates this awesome readme file. </dd>
  
  <dt> Circadian Lighting </dt>
  
  <dt> Fontawesome icons </dt>
  
  <dt> SmartThinQ LGE Sensors </dt>
  
  <dt> Rainforest </dt>
  </dt>



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

All of my configuration files are tested against the most stable version of home-assistant using [Github Actions](https://github.com/brianhanifin/Home-Assistant-Config/actions).


[lovelace-00]: ./README-images/_one_page_ui.jpeg
[lovelace-00t]: ./README-images/_one_page_ui_t.jpeg

[amazon-echo]: ./README-images/echo.jpeg
[bedroom_switches]: ./README-images/xiaomi_double_switch.jpeg
[button-medicine]: ./README-images/button_medicine.jpeg

[ha-version]: https://www.home-assistant.io/blog/categories/release-notes/
[ha-version-shield]: https://img.shields.io/badge/Home_Assistant-0.108.9-41BDF5?logo=home%20assistant

[github-build-status]: https://github.com/brianhanifin/Home-Assistant-Config/actions?workflow=build
[github-build-status-shield]: https://github.com/brianhanifin/Home-Assistant-Config/workflows/build/badge.svg

[commits-shield]: https://img.shields.io/github/commit-activity/m/brianhanifin/Home-Assistant-Config.svg?logo=github&logoColor=838B95
[commits]: https://github.com/brianhanifin/Home-Assistant-Config/pulse

[maintained]: https://img.shields.io/maintenance/yes/2020.svg

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