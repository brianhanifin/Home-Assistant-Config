$(function(){ //DOM Ready

    function navigate(url)
    {
        window.location.href = url;
    }

    $(document).attr("title", "Home");
    content_width = (120 + 5) * 4 + 5
    $('.gridster').width(content_width)
    $(".gridster ul").gridster({
        widget_margins: [5, 5],
        widget_base_dimensions: [120, 120],
        avoid_overlapped_widgets: true,
        max_rows: 15,
        max_size_x: 4,
        shift_widgets_up: false
    }).data('gridster').disable();
    
    // Add Widgets

    var gridster = $(".gridster ul").gridster().data('gridster');
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basedisplay-default-label" id="default-label"><h1 class="title" data-bind="text: title, attr:{ style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{ style: title2_style}"></h1><div class="valueunit" data-bind="attr:{ style: container_style}"><h2 class="value" data-bind="html: value, attr:{ style: value_style}"></h2><p class="unit" data-bind="html: unit, attr:{ style: unit_style}"></p></div><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 3, 1, 1, 1)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baselight-default-family-room-light" id="default-family-room-light"><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><span class="toggle-area" id="switch"></span><p class="state_text" data-bind="text: state_text, attr:{style: state_text_style}"></p><div class="levelunit"><p class="level" data-bind="text: level, attr:{style: level_style}"></p><p class="unit" data-bind="html: units, attr:{style: unit_style}"></p></div><p class="secondary-icon minus"><i data-bind="attr: {class: icon_down, style: level_down_style}" id="level-down"></i></p><p class="secondary-icon plus"><i data-bind="attr: {class: icon_up, style: level_up_style}" id="level-up"></i></p></div></li>', 1, 1, 1, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baselight-default-dining-room-light" id="default-dining-room-light"><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><span class="toggle-area" id="switch"></span><p class="state_text" data-bind="text: state_text, attr:{style: state_text_style}"></p><div class="levelunit"><p class="level" data-bind="text: level, attr:{style: level_style}"></p><p class="unit" data-bind="html: units, attr:{style: unit_style}"></p></div><p class="secondary-icon minus"><i data-bind="attr: {class: icon_down, style: level_down_style}" id="level-down"></i></p><p class="secondary-icon plus"><i data-bind="attr: {class: icon_up, style: level_up_style}" id="level-up"></i></p></div></li>', 1, 1, 2, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baselight-default-living-room-light" id="default-living-room-light"><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><span class="toggle-area" id="switch"></span><p class="state_text" data-bind="text: state_text, attr:{style: state_text_style}"></p><div class="levelunit"><p class="level" data-bind="text: level, attr:{style: level_style}"></p><p class="unit" data-bind="html: units, attr:{style: unit_style}"></p></div><p class="secondary-icon minus"><i data-bind="attr: {class: icon_down, style: level_down_style}" id="level-down"></i></p><p class="secondary-icon plus"><i data-bind="attr: {class: icon_up, style: level_up_style}" id="level-up"></i></p></div></li>', 1, 1, 3, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-kitchen-stove-light" id="default-kitchen-stove-light"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 1, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-kitchen-prep-light" id="default-kitchen-prep-light"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 2, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-living-room-fan" id="default-living-room-fan"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 3, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baselight-default-computer-desk-light" id="default-computer-desk-light"><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><span class="toggle-area" id="switch"></span><p class="state_text" data-bind="text: state_text, attr:{style: state_text_style}"></p><div class="levelunit"><p class="level" data-bind="text: level, attr:{style: level_style}"></p><p class="unit" data-bind="html: units, attr:{style: unit_style}"></p></div><p class="secondary-icon minus"><i data-bind="attr: {class: icon_down, style: level_down_style}" id="level-down"></i></p><p class="secondary-icon plus"><i data-bind="attr: {class: icon_up, style: level_up_style}" id="level-up"></i></p></div></li>', 1, 1, 1, 4)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baselight-default-play-room-light" id="default-play-room-light"><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><span class="toggle-area" id="switch"></span><p class="state_text" data-bind="text: state_text, attr:{style: state_text_style}"></p><div class="levelunit"><p class="level" data-bind="text: level, attr:{style: level_style}"></p><p class="unit" data-bind="html: units, attr:{style: unit_style}"></p></div><p class="secondary-icon minus"><i data-bind="attr: {class: icon_down, style: level_down_style}" id="level-down"></i></p><p class="secondary-icon plus"><i data-bind="attr: {class: icon_up, style: level_up_style}" id="level-up"></i></p></div></li>', 1, 1, 2, 4)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-scene-good-night" id="default-scene-good-night"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 3, 4)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-device-tracker-brian" id="default-device-tracker-brian"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 1, 5)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-device-tracker-nerene" id="default-device-tracker-nerene"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 2, 5)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-input-boolean-guest-mode" id="default-input-boolean-guest-mode"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 3, 5)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-cover-garage-door" id="default-cover-garage-door"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 1, 6)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-tv-livingroom" id="default-tv-livingroom"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 2, 6)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-tv-playroom" id="default-tv-playroom"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 3, 6)
    
    
    
    var widgets = {}
    // Initialize Widgets
    
        widgets["default-label"] = new basedisplay("default-label", "", "default", {'widget_type': 'basedisplay', 'fields': {'title': '', 'title2': '', 'value': 'Home', 'unit': '', 'state_text': ''}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'unit_style': '', 'value_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;', 'container_style': ''}, 'css': {}, 'icons': [], 'static_icons': [], 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-family-room-light"] = new baselight("default-family-room-light", "", "default", {'widget_type': 'baselight', 'entity': 'light.family_room_light', 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'light.family_room_light'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'light.family_room_light'}, 'fields': {'title': 'Family Room', 'title2': '', 'icon': '', 'units': '%', 'level': '', 'state_text': '', 'icon_style': ''}, 'icons': {'icon_on': 'mdi-lightbulb-on', 'icon_off': 'mdi-lightbulb-outline'}, 'static_icons': {'icon_up': 'fa-plus', 'icon_down': 'fa-minus'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'level_style': 'color: #fff;', 'unit_style': 'color: #fff;', 'level_up_style': 'color: #888;', 'level_down_style': 'color: #888;', 'widget_style': 'background-color: #444;'}, 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-dining-room-light"] = new baselight("default-dining-room-light", "", "default", {'widget_type': 'baselight', 'entity': 'light.dining_room_light', 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'light.dining_room_light'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'light.dining_room_light'}, 'fields': {'title': 'Dining Room', 'title2': '', 'icon': '', 'units': '%', 'level': '', 'state_text': '', 'icon_style': ''}, 'icons': {'icon_on': 'mdi-lightbulb-on', 'icon_off': 'mdi-lightbulb-outline'}, 'static_icons': {'icon_up': 'fa-plus', 'icon_down': 'fa-minus'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'level_style': 'color: #fff;', 'unit_style': 'color: #fff;', 'level_up_style': 'color: #888;', 'level_down_style': 'color: #888;', 'widget_style': 'background-color: #444;'}, 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-living-room-light"] = new baselight("default-living-room-light", "", "default", {'widget_type': 'baselight', 'entity': 'light.living_room_light', 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'light.living_room_light'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'light.living_room_light'}, 'fields': {'title': 'Living Room', 'title2': '', 'icon': '', 'units': '%', 'level': '', 'state_text': '', 'icon_style': ''}, 'icons': {'icon_on': 'mdi-lightbulb-on', 'icon_off': 'mdi-lightbulb-outline'}, 'static_icons': {'icon_up': 'fa-plus', 'icon_down': 'fa-minus'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'level_style': 'color: #fff;', 'unit_style': 'color: #fff;', 'level_up_style': 'color: #888;', 'level_down_style': 'color: #888;', 'widget_style': 'background-color: #444;'}, 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-kitchen-stove-light"] = new baseswitch("default-kitchen-stove-light", "", "default", {'widget_type': 'baseswitch', 'entity': 'switch.kitchen_stove_light', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'switch.kitchen_stove_light'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'switch.kitchen_stove_light'}, 'fields': {'title': 'Kitchen', 'title2': 'Stove Light', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'mdi-lightbulb-on', 'icon_off': 'mdi-lightbulb-outline'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;'}, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-kitchen-prep-light"] = new baseswitch("default-kitchen-prep-light", "", "default", {'widget_type': 'baseswitch', 'entity': 'switch.kitchen_prep_light', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'switch.kitchen_prep_light'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'switch.kitchen_prep_light'}, 'fields': {'title': 'Kitchen', 'title2': 'Prep Light', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'mdi-lightbulb-on', 'icon_off': 'mdi-lightbulb-outline'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;'}, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-living-room-fan"] = new baseswitch("default-living-room-fan", "", "default", {'widget_type': 'baseswitch', 'entity': 'switch.living_room_fan', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'switch.living_room_fan'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'switch.living_room_fan'}, 'fields': {'title': 'Living Room', 'title2': 'Fan', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'mdi-fan', 'icon_off': 'mdi-fan'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;'}, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-computer-desk-light"] = new baselight("default-computer-desk-light", "", "default", {'widget_type': 'baselight', 'entity': 'light.computer_desk_light', 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'light.computer_desk_light'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'light.computer_desk_light'}, 'fields': {'title': 'Computer Desk', 'title2': '', 'icon': '', 'units': '%', 'level': '', 'state_text': '', 'icon_style': ''}, 'icons': {'icon_on': 'mdi-lightbulb-on', 'icon_off': 'mdi-lightbulb-outline'}, 'static_icons': {'icon_up': 'fa-plus', 'icon_down': 'fa-minus'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'level_style': 'color: #fff;', 'unit_style': 'color: #fff;', 'level_up_style': 'color: #888;', 'level_down_style': 'color: #888;', 'widget_style': 'background-color: #444;'}, 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-play-room-light"] = new baselight("default-play-room-light", "", "default", {'widget_type': 'baselight', 'entity': 'light.play_room_light', 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'light.play_room_light'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'light.play_room_light'}, 'fields': {'title': 'Play Room', 'title2': '', 'icon': '', 'units': '%', 'level': '', 'state_text': '', 'icon_style': ''}, 'icons': {'icon_on': 'mdi-lightbulb-on', 'icon_off': 'mdi-lightbulb-outline'}, 'static_icons': {'icon_up': 'fa-plus', 'icon_down': 'fa-minus'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'level_style': 'color: #fff;', 'unit_style': 'color: #fff;', 'level_up_style': 'color: #888;', 'level_down_style': 'color: #888;', 'widget_style': 'background-color: #444;'}, 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-scene-good-night"] = new baseswitch("default-scene-good-night", "", "default", {'widget_type': 'baseswitch', 'entity': 'scene.good_night', 'state_inactive': 'scening', 'state_active': 'stillscening', 'enable': 1, 'momentary': 1000, 'ignore_state': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'scene.good_night'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'scene.good_night'}, 'fields': {'title': '', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fa-square', 'icon_off': 'fa-square'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;'}, 'title_is_friendly_name': 1, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-device-tracker-brian"] = new baseswitch("default-device-tracker-brian", "", "default", {'widget_type': 'baseswitch', 'entity': 'device_tracker.brian', 'state_active': 'home', 'state_inactive': 'not_home', 'enable': 0, 'state_text': 1, 'post_service_active': {'service': 'device_tracker/see', 'dev_id': '', 'location_name': 'home'}, 'post_service_inactive': {'service': 'device_tracker/see', 'dev_id': '', 'location_name': 'not_home'}, 'fields': {'title': '', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fa-user', 'icon_off': 'fa-user'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;'}, 'state_map': {'home': 'HOME', 'not_home': 'AWAY'}, 'title_is_friendly_name': 1, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-device-tracker-nerene"] = new baseswitch("default-device-tracker-nerene", "", "default", {'widget_type': 'baseswitch', 'entity': 'device_tracker.nerene', 'state_active': 'home', 'state_inactive': 'not_home', 'enable': 0, 'state_text': 1, 'post_service_active': {'service': 'device_tracker/see', 'dev_id': '', 'location_name': 'home'}, 'post_service_inactive': {'service': 'device_tracker/see', 'dev_id': '', 'location_name': 'not_home'}, 'fields': {'title': '', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fa-user', 'icon_off': 'fa-user'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;'}, 'state_map': {'home': 'HOME', 'not_home': 'AWAY'}, 'title_is_friendly_name': 1, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-input-boolean-guest-mode"] = new baseswitch("default-input-boolean-guest-mode", "", "default", {'widget_type': 'baseswitch', 'entity': 'input_boolean.guest_mode', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'input_boolean.guest_mode'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'input_boolean.guest_mode'}, 'fields': {'title': '', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fa-sliders', 'icon_off': 'fa-sliders'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;'}, 'title_is_friendly_name': 1, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-cover-garage-door"] = new baseswitch("default-cover-garage-door", "", "default", {'widget_type': 'baseswitch', 'entity': 'cover.garage_door', 'state_active': 'open', 'state_inactive': 'closed', 'enable': 1, 'post_service_active': {'service': 'cover/open_cover', 'entity_id': 'cover.garage_door'}, 'post_service_inactive': {'service': 'cover/close_cover', 'entity_id': 'cover.garage_door'}, 'fields': {'title': '', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fa-arrows-v', 'icon_off': 'fa-arrows-v'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #ff0055;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;'}, 'title_is_friendly_name': 1, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-tv-livingroom"] = new baseswitch("default-tv-livingroom", "", "default", {'widget_type': 'baseswitch', 'entity': 'switch.livingroom_tv', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'switch.livingroom_tv'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'switch.livingroom_tv'}, 'fields': {'title': 'Living Room', 'title2': 'TV', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'mdi-television', 'icon_off': 'mdi-television'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;'}, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    
        widgets["default-tv-playroom"] = new baseswitch("default-tv-playroom", "", "default", {'widget_type': 'baseswitch', 'entity': 'switch.playroom_tv', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'switch.playroom_tv'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'switch.playroom_tv'}, 'fields': {'title': 'Play Room', 'title2': 'TV', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'mdi-television', 'icon_off': 'mdi-television'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;'}, 'use_comma': 0, 'precision': 1, 'use_hass_icon': 1, 'namespace': 'default'})
    

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
    ha_status(stream_url, "Home", widgets);

});