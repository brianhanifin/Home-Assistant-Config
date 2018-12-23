$(function(){ //DOM Ready

    function navigate(url)
    {
        window.location.href = url;
    }

    $(document).attr("title", "Control");
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
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-fan-living-room" id="default-fan-living-room"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 1, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baselight-default-living-room-light" id="default-living-room-light"><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><span class="toggle-area" id="switch"></span><p class="state_text" data-bind="text: state_text, attr:{style: state_text_style}"></p><div class="levelunit"><p class="level" data-bind="text: level, attr:{style: level_style}"></p><p class="unit" data-bind="html: units, attr:{style: unit_style}"></p></div><p class="secondary-icon minus"><i data-bind="attr: {class: icon_down, style: level_down_style}" id="level-down"></i></p><p class="secondary-icon plus"><i data-bind="attr: {class: icon_up, style: level_up_style}" id="level-up"></i></p></div></li>', 1, 1, 2, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baselight-default-family-room-light" id="default-family-room-light"><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><span class="toggle-area" id="switch"></span><p class="state_text" data-bind="text: state_text, attr:{style: state_text_style}"></p><div class="levelunit"><p class="level" data-bind="text: level, attr:{style: level_style}"></p><p class="unit" data-bind="html: units, attr:{style: unit_style}"></p></div><p class="secondary-icon minus"><i data-bind="attr: {class: icon_down, style: level_down_style}" id="level-down"></i></p><p class="secondary-icon plus"><i data-bind="attr: {class: icon_up, style: level_up_style}" id="level-up"></i></p></div></li>', 1, 1, 3, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-good-night" id="default-good-night"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 1, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baselight-default-brians-light" id="default-brians-light"><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><span class="toggle-area" id="switch"></span><p class="state_text" data-bind="text: state_text, attr:{style: state_text_style}"></p><div class="levelunit"><p class="level" data-bind="text: level, attr:{style: level_style}"></p><p class="unit" data-bind="html: units, attr:{style: unit_style}"></p></div><p class="secondary-icon minus"><i data-bind="attr: {class: icon_down, style: level_down_style}" id="level-down"></i></p><p class="secondary-icon plus"><i data-bind="attr: {class: icon_up, style: level_up_style}" id="level-up"></i></p></div></li>', 1, 1, 2, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baselight-default-bedroom-light" id="default-bedroom-light"><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><span class="toggle-area" id="switch"></span><p class="state_text" data-bind="text: state_text, attr:{style: state_text_style}"></p><div class="levelunit"><p class="level" data-bind="text: level, attr:{style: level_style}"></p><p class="unit" data-bind="html: units, attr:{style: unit_style}"></p></div><p class="secondary-icon minus"><i data-bind="attr: {class: icon_down, style: level_down_style}" id="level-down"></i></p><p class="secondary-icon plus"><i data-bind="attr: {class: icon_up, style: level_up_style}" id="level-up"></i></p></div></li>', 1, 1, 3, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-presence-guests" id="default-presence-guests"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 1, 4)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-presence-brian" id="default-presence-brian"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 2, 4)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-presence-nerene" id="default-presence-nerene"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 3, 4)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-home" id="default-nav-home"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 1, 5)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-devices" id="default-nav-devices"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 2, 5)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-lights" id="default-nav-lights"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 3, 5)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-outside" id="default-nav-outside"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 1, 6)
    
    
    
    var widgets = {}
    // Initialize Widgets
    
        widgets["default-label"] = new basedisplay("default-label", "", "obsidian", {'widget_type': 'basedisplay', 'fields': {'title': '', 'title2': '', 'value': 'Control Panel', 'unit': '', 'state_text': ''}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'unit_style': '', 'value_style': 'color: #00FFFF;', 'state_text_style': 'color: #00FFFF;', 'widget_style': 'background-image: url(css/obsidian/img/obsidian_w_bg.jpg);background: #444;', 'container_style': ''}, 'css': {}, 'icons': [], 'static_icons': [], 'widget_style': 'background: #444;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1})
    
        widgets["default-fan-living-room"] = new baseswitch("default-fan-living-room", "", "obsidian", {'widget_type': 'baseswitch', 'entity': 'switch.living_room_fan', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'switch.living_room_fan'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'switch.living_room_fan'}, 'fields': {'title': 'Living Room', 'title2': 'Fan', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'mdi-fan', 'icon_off': 'mdi-fan'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #00FFFF;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #00FFFF;', 'widget_style': 'background-image: url(css/obsidian/img/obsidian_w_bg.jpg);background: #333;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-living-room-light"] = new baselight("default-living-room-light", "", "obsidian", {'widget_type': 'baselight', 'entity': 'light.living_room_light', 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'light.living_room_light'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'light.living_room_light'}, 'fields': {'title': 'Living Room', 'title2': '', 'icon': '', 'units': '%', 'level': '', 'state_text': '', 'icon_style': ''}, 'icons': {'icon_on': 'mdi-lightbulb-on', 'icon_off': 'mdi-lightbulb-outline'}, 'static_icons': {'icon_up': 'fa-plus', 'icon_down': 'fa-minus'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #00FFFF;', 'level_style': 'color: #888;', 'unit_style': 'color: #888;', 'level_up_style': 'color: #888;', 'level_down_style': 'color: #888;', 'widget_style': 'background-image: url(css/obsidian/img/obsidian_w_bg.jpg);background: #333;'}, 'css': {'icon_style_active': 'color: #00FFFF;', 'icon_style_inactive': 'color: #888;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-family-room-light"] = new baselight("default-family-room-light", "", "obsidian", {'widget_type': 'baselight', 'entity': 'light.family_room_light', 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'light.family_room_light'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'light.family_room_light'}, 'fields': {'title': 'Family Room', 'title2': '', 'icon': '', 'units': '%', 'level': '', 'state_text': '', 'icon_style': ''}, 'icons': {'icon_on': 'mdi-lightbulb-on', 'icon_off': 'mdi-lightbulb-outline'}, 'static_icons': {'icon_up': 'fa-plus', 'icon_down': 'fa-minus'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #00FFFF;', 'level_style': 'color: #888;', 'unit_style': 'color: #888;', 'level_up_style': 'color: #888;', 'level_down_style': 'color: #888;', 'widget_style': 'background-image: url(css/obsidian/img/obsidian_w_bg.jpg);background: #333;'}, 'css': {'icon_style_active': 'color: #00FFFF;', 'icon_style_inactive': 'color: #888;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-good-night"] = new baseswitch("default-good-night", "", "obsidian", {'widget_type': 'baseswitch', 'entity': 'scene.good_night', 'state_inactive': 'scening', 'state_active': 'stillscening', 'enable': 1, 'momentary': 1000, 'ignore_state': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'scene.good_night'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'scene.good_night'}, 'fields': {'title': 'Good Night', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'mdi-weather-night', 'icon_off': 'mdi-weather-night'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #00FFFF;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #00FFFF;', 'widget_style': 'background-image: url(css/obsidian/img/obsidian_w_bg.jpg);background: #333;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-brians-light"] = new baselight("default-brians-light", "", "obsidian", {'widget_type': 'baselight', 'entity': 'light.brians_light', 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'light.brians_light'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'light.brians_light'}, 'fields': {'title': "Brian's Light", 'title2': '', 'icon': '', 'units': '%', 'level': '', 'state_text': '', 'icon_style': ''}, 'icons': {'icon_on': 'mdi-lightbulb-on', 'icon_off': 'mdi-lightbulb-outline'}, 'static_icons': {'icon_up': 'fa-plus', 'icon_down': 'fa-minus'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #00FFFF;', 'level_style': 'color: #888;', 'unit_style': 'color: #888;', 'level_up_style': 'color: #888;', 'level_down_style': 'color: #888;', 'widget_style': 'background-image: url(css/obsidian/img/obsidian_w_bg.jpg);background: #333;'}, 'css': {'icon_style_active': 'color: #00FFFF;', 'icon_style_inactive': 'color: #888;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-bedroom-light"] = new baselight("default-bedroom-light", "", "obsidian", {'widget_type': 'baselight', 'entity': 'light.bedroom_light', 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'light.bedroom_light'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'light.bedroom_light'}, 'fields': {'title': 'Bedroom', 'title2': '', 'icon': '', 'units': '%', 'level': '', 'state_text': '', 'icon_style': ''}, 'icons': {'icon_on': 'mdi-lightbulb-on', 'icon_off': 'mdi-lightbulb-outline'}, 'static_icons': {'icon_up': 'fa-plus', 'icon_down': 'fa-minus'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #00FFFF;', 'level_style': 'color: #888;', 'unit_style': 'color: #888;', 'level_up_style': 'color: #888;', 'level_down_style': 'color: #888;', 'widget_style': 'background-image: url(css/obsidian/img/obsidian_w_bg.jpg);background: #333;'}, 'css': {'icon_style_active': 'color: #00FFFF;', 'icon_style_inactive': 'color: #888;'}, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-presence-guests"] = new baseswitch("default-presence-guests", "", "obsidian", {'widget_type': 'baseswitch', 'entity': 'binary_sensor.presence_guests', 'state_active': 'on', 'state_inactive': 'off', 'fields': {'title': 'Guests', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fa-users', 'icon_off': 'fa-users'}, 'static_icons': [], 'css': {'icon_style_active': 'color: lightblue;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #00FFFF;', 'widget_style': 'background-image: url(css/obsidian/img/obsidian_w_bg.jpg);background: #333;'}, 'icon_style_active': 'color: lightblue;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-presence-brian"] = new baseswitch("default-presence-brian", "", "obsidian", {'widget_type': 'baseswitch', 'entity': 'binary_sensor.presence_brian', 'state_active': 'on', 'state_inactive': 'off', 'fields': {'title': 'Brian', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fa-male', 'icon_off': 'fa-male'}, 'static_icons': [], 'css': {'icon_style_active': 'color: lightblue;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #00FFFF;', 'widget_style': 'background-image: url(css/obsidian/img/obsidian_w_bg.jpg);background: #333;'}, 'icon_style_active': 'color: lightblue;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-presence-nerene"] = new baseswitch("default-presence-nerene", "", "obsidian", {'widget_type': 'baseswitch', 'entity': 'binary_sensor.presence_nerene', 'state_active': 'on', 'state_inactive': 'off', 'fields': {'title': 'Nerene', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fa-female', 'icon_off': 'fa-female'}, 'static_icons': [], 'css': {'icon_style_active': 'color: pink;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #00FFFF;', 'widget_style': 'background-image: url(css/obsidian/img/obsidian_w_bg.jpg);background: #333;'}, 'icon_style_active': 'color: pink;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-nav-home"] = new basejavascript("default-nav-home", "", "obsidian", {'widget_type': 'basejavascript', 'fields': {'title': 'Home', 'title2': '', 'icon': '', 'icon_style': ''}, 'icons': {'icon_active': 'fa-spinner fa-spin', 'icon_inactive': 'fa-gear'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'widget_style': 'background: #444;background-image: none;color: black;border-style: inset;'}, 'css': {'icon_active_style': 'color: #00FFFF;', 'icon_inactive_style': 'color: #00FFFF;'}, 'static_icons': [], 'dashboard': 'home', 'widget_style': 'background: #444;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1})
    
        widgets["default-nav-devices"] = new basejavascript("default-nav-devices", "", "obsidian", {'widget_type': 'basejavascript', 'fields': {'title': 'Devices', 'title2': '', 'icon': '', 'icon_style': ''}, 'icons': {'icon_active': 'fa-spinner fa-spin', 'icon_inactive': 'fa-gear'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'widget_style': 'background: #444;background-image: none;color: black;border-style: inset;'}, 'css': {'icon_active_style': 'color: #00FFFF;', 'icon_inactive_style': 'color: #00FFFF;'}, 'static_icons': [], 'dashboard': 'devices', 'widget_style': 'background: #444;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1})
    
        widgets["default-nav-lights"] = new basejavascript("default-nav-lights", "", "obsidian", {'widget_type': 'basejavascript', 'fields': {'title': 'Lights', 'title2': '', 'icon': '', 'icon_style': ''}, 'icons': {'icon_active': 'fa-spinner fa-spin', 'icon_inactive': 'fa-gear'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'widget_style': 'background: #444;background-image: none;color: black;border-style: inset;'}, 'css': {'icon_active_style': 'color: #00FFFF;', 'icon_inactive_style': 'color: #00FFFF;'}, 'static_icons': [], 'dashboard': 'lights', 'widget_style': 'background: #444;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1})
    
        widgets["default-nav-outside"] = new basejavascript("default-nav-outside", "", "obsidian", {'widget_type': 'basejavascript', 'fields': {'title': 'Outside', 'title2': '', 'icon': '', 'icon_style': ''}, 'icons': {'icon_active': 'fa-spinner fa-spin', 'icon_inactive': 'fa-gear'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'widget_style': 'background: #444;background-image: none;color: black;border-style: inset;'}, 'css': {'icon_active_style': 'color: #00FFFF;', 'icon_inactive_style': 'color: #00FFFF;'}, 'static_icons': [], 'dashboard': 'outside', 'widget_style': 'background: #444;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1})
    

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
    ha_status(stream_url, "Control", widgets);

});