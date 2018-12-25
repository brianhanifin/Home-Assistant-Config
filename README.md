# Hanifin Smart Home

[![travis build status][travis-build-status-shield]][travis-build-status] [![last commit time][github-last-commit]][github-master] [![GitHub Activity][commits-shield]][commits]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

## Lovelace Interface
![home][lovelace-0] ![wakeup][lovelace-2]

## About our smart home
I started using Home Assistant in the spring of 2018 when I outgrew the limited automations on Apple's HomeKit platform. While my Home Assistant initially included many HomeKit smart plugs, I eventually moved away from the platform altogether.

Home Assistant now manages our smart home devices with lots of intelligence handled by my automations. It is important that our devices can be controlled by standard wall switches where possible, but we use Alexa to control our devices with our voice. Not only can we talk to Alexa, but she can let us know when the laundry wash cycle is complete (thanks to the help of a power monitoring smart plug).

### Insteon
I started with HomeKit compatible *Insteon* in-wall dimmer switches and in-wall wireless remotes. The remotes are installed in several locations that otherwise would not have a light switch. Somehow our living room never had a light switch installed, now it does.

### Z-Wave
I have decided that I prefer the look of the GE Z-Wave in-wall dimmers and switches over the four button Insteon dimmers because they are easier for guests to understand.

### Philips Hue
Hue color bulbs for Porch Light and Garage Door Entry downlight. The former changes color based on the current national holiday (or family birthday/anniversary) while the later pulses changing colors to give us a heads up that the garage door is open. Two of my remaining six Hue bulbs are reserved for an additional two porch/entryway hanging lamps.

### ZigBee/Hue Compabile Light Strips
I followed [this guide][hue-strip-guide] to build an inexpensive color changing light strip that is installed under our kitchen cabinets. This light is motion controlled, so we can fill our cup with water at night. The light gets brighter when either of the kitchen lights are turned on, and dim again when they are off.

I plan to build one more strip to light the inside of our pantry. I will be using a wireless contact sensor to turn the lights on and off.

### Xiaomi
This Chinese company makes a lot of very useful and inexpensive wireless smart home products. I use their Zigbee smart hub to get these devices to talk to Home Assistant.
#### Motion Sensor
Two motion sensors watch for people to enter the kitchen so they can turn on the undercabinet light strip.
#### Contact Sensor
I use their door/window sensors to turn the light in the shoe closet on and off, and remind us when we leave the Glowforge vent window open.
#### Leak Sensor
As soon as we finished our Kitchen remodel I set one of these wireless little dics under the sink. Should water pool and activate the senor a Home Assistant "Watch Dog" will instantly have Alexa announce there is a water leak all over the house, and an alert will be sent to my phone!

I ordered a few more so I could have better leak coverage around the house, including the water heater tray. We had a water heater leak slowly over the summer and we didn't realize it until it got worse. I would also use one of these senors in reverse to have Alexa let us know when it is time to refill the dog's water bowl.

### SonOff with Tasmota
I replaced my HomeKit smart plugs with various SonOff plugs with Tasmota installed. 

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

### Frenk
I just learned of Franck recently, but he is a long time member of the community. I just refactored my code to be similar to his config ([as discussed in this video][frenk-youtube-config]).
* Github: [Frenck's Home Assistant Configuration][frenk-github]
* YouTube: [Frenk's Channel][frenk-youtube]


[lovelace-0]: ./README-images/0.png
[lovelace-2]: ./README-images/2.png

[commits-shield]: https://img.shields.io/github/commit-activity/y/brianhanifin/Home-AssistantConfig.svg
[commits]: https://github.com/brianhanifin/Home-AssistantConfig/commits/master
[github-last-commit]: https://img.shields.io/github/last-commit/BrianHanifin/Home-AssistantConfig.svg?style=plasticr
[github-master]: https://github.com/BrianHanifin/Home-AssistantConfig/commits/master
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg
[discord]: https://discord.gg/c5DvZ4e
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg
[forum]: https://community.home-assistant.io/u/brianhanifin/summary
[hue-strip-guide]:https://char.gd/blog/2018/building-better-cheaper-philips-hue-led-strips
[travis-build-status]: https://travis-ci.org/brianhanifin/Home-AssistantConfig
[travis-build-status-shield]: https://travis-ci.org/brianhanifin/Home-AssistantConfig.svg?branch=master

[carlo-blog]: https://www.vcloudinfo.com
[carlo-github]: https://github.com/CCOSTAN/Home-AssistantConfig
[carlo-youtube]: https://YouTube.com/vCloudInfo

[drzzs-github]: https://github.com/Snipercaine
[drzzs-youtube]: https://www.youtube.com/channel/UC7G4tLa4Kt6A9e3hJ-HO8ng

[frenk-github]: https://github.com/frenck/home-assistant-config/
[frenk-youtube]: https://www.youtube.com/user/Frenck
[frenk-youtube-config]: https://youtu.be/lndeybw21PY