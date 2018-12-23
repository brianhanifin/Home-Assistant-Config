$(function(){ //DOM Ready

    function navigate(url)
    {
        window.location.href = url;
    }

    $(document).attr("title", "Devices");
    content_width = (120 + 5) * 3 + 5
    $('.gridster').width(content_width)
    $(".gridster ul").gridster({
        widget_margins: [5, 5],
        widget_base_dimensions: [120, 120],
        avoid_overlapped_widgets: true,
        max_rows: 15,
        max_size_x: 3,
        shift_widgets_up: false
    }).data('gridster').disable();
    
    // Add Widgets

    var gridster = $(".gridster ul").gridster().data('gridster');
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basedisplay-default-label" id="default-label"><h1 class="title" data-bind="text: title, attr:{ style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{ style: title2_style}"></h1><div class="valueunit" data-bind="attr:{ style: container_style}"><h2 class="value" data-bind="html: value, attr:{ style: value_style}"></h2><p class="unit" data-bind="html: unit, attr:{ style: unit_style}"></p></div><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 3, 1, 1, 1)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-fan-master-bedroom" id="default-fan-master-bedroom"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 1, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-fan-living-room" id="default-fan-living-room"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 2, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-front-door-lock" id="default-front-door-lock"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 3, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-garage-door" id="default-garage-door"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 1, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-hot-water-pump" id="default-hot-water-pump"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 2, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseclimate-default-thermostat1" id="default-thermostat1"><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><div class="levelunit"><h2 class="level" data-bind="text: level, attr:{ style: level_style}"></h2><p class="unit" data-bind="html: unit, attr:{ style: unit_style}"></p></div><div class="levelunit2"><p class="level2" data-bind="text: level2, attr:{style: level2_style}"></p><p class="unit2" data-bind="html: unit, attr:{style: unit2_style}"></p></div><p class="secondary-icon minus"><i data-bind="attr: {class: icon_down, style: level_down_style}" id="level-down"></i></p><p class="secondary-icon plus"><i data-bind="attr: {class: icon_up, style: level_up_style}" id="level-up"></i></p></div></li>', 1, 1, 3, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseclimate-default-thermostat2" id="default-thermostat2"><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><div class="levelunit"><h2 class="level" data-bind="text: level, attr:{ style: level_style}"></h2><p class="unit" data-bind="html: unit, attr:{ style: unit_style}"></p></div><div class="levelunit2"><p class="level2" data-bind="text: level2, attr:{style: level2_style}"></p><p class="unit2" data-bind="html: unit, attr:{style: unit2_style}"></p></div><p class="secondary-icon minus"><i data-bind="attr: {class: icon_down, style: level_down_style}" id="level-down"></i></p><p class="secondary-icon plus"><i data-bind="attr: {class: icon_up, style: level_up_style}" id="level-up"></i></p></div></li>', 1, 1, 1, 4)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-tv-livingroom" id="default-tv-livingroom"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 2, 4)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-tv-playroom" id="default-tv-playroom"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 3, 4)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-home" id="default-nav-home"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 1, 5)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-devices" id="default-nav-devices"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 2, 5)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-lights" id="default-nav-lights"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 3, 5)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-outside" id="default-nav-outside"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 1, 6)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-modes" id="default-nav-modes"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 2, 6)
    
    
    
    var widgets = {}
    // Initialize Widgets
    
        widgets["default-label"] = new basedisplay("default-label", "", "default", {'widget_type': 'basedisplay', 'fields': {'title': '', 'title2': '', 'value': 'Devices', 'unit': '', 'state_text': ''}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'unit_style': '', 'value_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #444;', 'container_style': ''}, 'css': {}, 'icons': [], 'static_icons': [], 'widget_style': 'background: #444;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1})
    
        widgets["default-fan-master-bedroom"] = new baseswitch("default-fan-master-bedroom", "", "default", {'widget_type': 'baseswitch', 'entity': 'switch.master_bedroom_fan', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'switch.master_bedroom_fan'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'switch.master_bedroom_fan'}, 'fields': {'title': 'Fan', 'title2': 'Bedroom', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'mdi-fan', 'icon_off': 'mdi-fan'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #333;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-fan-living-room"] = new baseswitch("default-fan-living-room", "", "default", {'widget_type': 'baseswitch', 'entity': 'switch.living_room_fan', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'switch.living_room_fan'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'switch.living_room_fan'}, 'fields': {'title': 'Fan', 'title2': 'Living Room', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'mdi-fan', 'icon_off': 'mdi-fan'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #333;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-front-door-lock"] = new baseswitch("default-front-door-lock", "", "default", {'widget_type': 'baseswitch', 'entity': 'lock.front_door', 'state_active': 'unlocked', 'state_inactive': 'locked', 'enable': 1, 'post_service_active': {'service': 'lock/unlock', 'entity_id': 'lock.front_door'}, 'post_service_inactive': {'service': 'lock/lock', 'entity_id': 'lock.front_door'}, 'fields': {'title': 'Front Door', 'title2': 'Lock', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'mdi-lock-open', 'icon_off': 'mdi-lock'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #ff0055;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #333;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-garage-door"] = new baseswitch("default-garage-door", "", "default", {'widget_type': 'baseswitch', 'entity': 'cover.garage_door', 'state_active': 'open', 'state_inactive': 'closed', 'enable': 1, 'post_service_active': {'service': 'cover/open_cover', 'entity_id': 'cover.garage_door'}, 'post_service_inactive': {'service': 'cover/close_cover', 'entity_id': 'cover.garage_door'}, 'fields': {'title': 'Garage Door', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'mdi-garage-open', 'icon_off': 'mdi-garage'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #ff0055;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #333;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-hot-water-pump"] = new baseswitch("default-hot-water-pump", "", "default", {'widget_type': 'baseswitch', 'entity': 'switch.sonoff_pow01', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'switch.sonoff_pow01'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'switch.sonoff_pow01'}, 'fields': {'title': 'Hot Water', 'title2': '(5m Timeout)', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fa-toggle-on', 'icon_off': 'fa-toggle-off'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #333;'}, 'icon_on': 'fa-toggle-on', 'icon_off': 'fa-toggle-off', 'use_hass_icon': 0, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'widget_style': 'background: #333;'})
    
        widgets["default-thermostat1"] = new baseclimate("default-thermostat1", "", "default", {'widget_type': 'baseclimate', 'entity': 'climate.home', 'post_service': {'service': 'climate/set_temperature', 'entity_id': 'climate.home'}, 'fields': {'title': 'Thermostat', 'title2': 'Home', 'unit': '', 'level': '', 'level2': ''}, 'icons': [], 'css': {}, 'static_icons': {'icon_up': 'fas-plus', 'icon_down': 'fas-minus'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'level_style': 'color: #00aaff;', 'level2_style': 'color: #00aaff;', 'level_up_style': 'color: #888;', 'level_down_style': 'color: #888;', 'widget_style': 'background-color: #444;background: #333;', 'unit_style': 'color: #00aaff;', 'unit2_style': 'color: #00aaff;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-thermostat2"] = new baseclimate("default-thermostat2", "", "default", {'widget_type': 'baseclimate', 'entity': 'climate.playroom', 'post_service': {'service': 'climate/set_temperature', 'entity_id': 'climate.playroom'}, 'fields': {'title': 'Thermostat', 'title2': 'Playroom', 'unit': '', 'level': '', 'level2': ''}, 'icons': [], 'css': {}, 'static_icons': {'icon_up': 'fas-plus', 'icon_down': 'fas-minus'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'level_style': 'color: #00aaff;', 'level2_style': 'color: #00aaff;', 'level_up_style': 'color: #888;', 'level_down_style': 'color: #888;', 'widget_style': 'background-color: #444;background: #333;', 'unit_style': 'color: #00aaff;', 'unit2_style': 'color: #00aaff;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-tv-livingroom"] = new baseswitch("default-tv-livingroom", "", "default", {'widget_type': 'baseswitch', 'entity': 'switch.livingroom_tv', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'switch.livingroom_tv'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'switch.livingroom_tv'}, 'fields': {'title': 'TV', 'title2': 'Living Room', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'mdi-television', 'icon_off': 'mdi-television'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #333;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-tv-playroom"] = new baseswitch("default-tv-playroom", "", "default", {'widget_type': 'baseswitch', 'entity': 'switch.playroom_tv', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'switch.playroom_tv'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'switch.playroom_tv'}, 'fields': {'title': 'TV', 'title2': 'Play Room', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'mdi-television', 'icon_off': 'mdi-television'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #333;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-nav-home"] = new basejavascript("default-nav-home", "", "default", {'widget_type': 'basejavascript', 'fields': {'title': 'Home', 'title2': '', 'icon': '', 'icon_style': ''}, 'icons': {'icon_active': 'mdi-arrow-right-bold-circle', 'icon_inactive': 'mdi-arrow-right-bold-circle'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #444;'}, 'css': {'icon_active_style': 'color: #fff;', 'icon_inactive_style': 'color: #fff;'}, 'static_icons': [], 'dashboard': 'home', 'icon_active': 'mdi-arrow-right-bold-circle', 'icon_inactive': 'mdi-arrow-right-bold-circle', 'widget_style': 'background: #444;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1})
    
        widgets["default-nav-devices"] = new basejavascript("default-nav-devices", "", "default", {'widget_type': 'basejavascript', 'fields': {'title': 'Devices', 'title2': '', 'icon': '', 'icon_style': ''}, 'icons': {'icon_active': 'mdi-arrow-right-bold-circle', 'icon_inactive': 'mdi-arrow-right-bold-circle'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #444;'}, 'css': {'icon_active_style': 'color: #fff;', 'icon_inactive_style': 'color: #fff;'}, 'static_icons': [], 'dashboard': 'devices', 'icon_active': 'mdi-arrow-right-bold-circle', 'icon_inactive': 'mdi-arrow-right-bold-circle', 'widget_style': 'background: #444;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1})
    
        widgets["default-nav-lights"] = new basejavascript("default-nav-lights", "", "default", {'widget_type': 'basejavascript', 'fields': {'title': 'Lights', 'title2': '', 'icon': '', 'icon_style': ''}, 'icons': {'icon_active': 'mdi-arrow-right-bold-circle', 'icon_inactive': 'mdi-arrow-right-bold-circle'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #444;'}, 'css': {'icon_active_style': 'color: #fff;', 'icon_inactive_style': 'color: #fff;'}, 'static_icons': [], 'dashboard': 'lights', 'icon_active': 'mdi-arrow-right-bold-circle', 'icon_inactive': 'mdi-arrow-right-bold-circle', 'widget_style': 'background: #444;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1})
    
        widgets["default-nav-outside"] = new basejavascript("default-nav-outside", "", "default", {'widget_type': 'basejavascript', 'fields': {'title': 'Outside', 'title2': '', 'icon': '', 'icon_style': ''}, 'icons': {'icon_active': 'mdi-arrow-right-bold-circle', 'icon_inactive': 'mdi-arrow-right-bold-circle'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #444;'}, 'css': {'icon_active_style': 'color: #fff;', 'icon_inactive_style': 'color: #fff;'}, 'static_icons': [], 'dashboard': 'outside', 'icon_active': 'mdi-arrow-right-bold-circle', 'icon_inactive': 'mdi-arrow-right-bold-circle', 'widget_style': 'background: #444;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1})
    
        widgets["default-nav-modes"] = new basejavascript("default-nav-modes", "", "default", {'widget_type': 'basejavascript', 'fields': {'title': 'Mode', 'title2': 'Overrides', 'icon': '', 'icon_style': ''}, 'icons': {'icon_active': 'mdi-arrow-right-bold-circle', 'icon_inactive': 'mdi-arrow-right-bold-circle'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #444;'}, 'css': {'icon_active_style': 'color: #fff;', 'icon_inactive_style': 'color: #fff;'}, 'static_icons': [], 'dashboard': 'modes', 'icon_active': 'mdi-arrow-right-bold-circle', 'icon_inactive': 'mdi-arrow-right-bold-circle', 'widget_style': 'background: #444;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1})
    

    // Setup click handler to cancel timeout navigations

    $( ".gridster" ).click(function(){
        clearTimeout(myTimeout);
        if (myTimeoutSticky) {
            myTimeout = setTimeout(function() { navigate(myTimeoutUrl); }, myTimeoutDelay);
        }
    });

    // Set up timeout

    var myTimeout;
    var myTimeoutUrl;
    var myTimeoutDelay;
    var myTimeoutSticky = 0;

    if (location.search != "")
    {
        var query = location.search.substr(1);
        var result = {};
        query.split("&").forEach(function(part) {
        var item = part.split("=");
        result[item[0]] = decodeURIComponent(item[1]);
        });

        if ("timeout" in result && "return" in result)
        {
            url = result.return
            argcount = 0
            for (arg in result)
            {
                if (arg != "timeout" && arg != "return" && arg != "sticky")
                {
                    if (argcount == 0)
                    {
                        url += "?";
                    }
                    else
                    {
                        url += "?";
                    }
                    argcount ++;
                    url += arg + "=" + result[arg]
                }
            }
            if ("sticky" in result)
            {
                myTimeoutSticky = (result.sticky == "1");
            }
            myTimeoutUrl = url;
            myTimeoutDelay = result.timeout * 1000;
            myTimeout = setTimeout(function() { navigate(url); }, result.timeout * 1000);
        }
    }

    // Start listening for HA Events
    if (location.protocol == 'https:')
    {
        wsprot = "wss:"
    }
    else
    {
        wsprot = "ws:"
    }
    var stream_url = wsprot + '//' + location.host + '/stream'
    ha_status(stream_url, "Devices", widgets);

});