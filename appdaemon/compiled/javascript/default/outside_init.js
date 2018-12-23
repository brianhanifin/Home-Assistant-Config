$(function(){ //DOM Ready

    function navigate(url)
    {
        window.location.href = url;
    }

    $(document).attr("title", "Outside");
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
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basedisplay-default-sensor-front-yard-next-cycle" id="default-sensor-front-yard-next-cycle"><h1 class="title" data-bind="text: title, attr:{ style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{ style: title2_style}"></h1><div class="valueunit" data-bind="attr:{ style: container_style}"><h2 class="value" data-bind="html: value, attr:{ style: value_style}"></h2><p class="unit" data-bind="html: unit, attr:{ style: unit_style}"></p></div><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 1, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-binary-sensor-front-yard-watering" id="default-binary-sensor-front-yard-watering"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 2, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-switch-front-yard-manual-watering" id="default-switch-front-yard-manual-watering"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 3, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basedisplay-default-sensor-pool-filler-next-cycle" id="default-sensor-pool-filler-next-cycle"><h1 class="title" data-bind="text: title, attr:{ style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{ style: title2_style}"></h1><div class="valueunit" data-bind="attr:{ style: container_style}"><h2 class="value" data-bind="html: value, attr:{ style: value_style}"></h2><p class="unit" data-bind="html: unit, attr:{ style: unit_style}"></p></div><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 1, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-binary-sensor-pool-filler-watering" id="default-binary-sensor-pool-filler-watering"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 2, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-switch-pool-filler-manual-watering" id="default-switch-pool-filler-manual-watering"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 3, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseweather-default-weather" id="default-weather"><h1 class="title" data-bind="text: title, attr:{ style: title_style}"></h1><div data-bind="attr: {style: main_style}"><p class="primary-climacon" data-bind="css: icon"></p><p class="primary-info" data-bind="text: temperature"></p><p class="primary-unit" data-bind="html: unit, attr: {style: unit_style}"></p><br></div><div data-bind="attr: {style: sub_style}"><p class="secondary-detail" data-bind="visible: apparent_temperature"><span class="secondary-icon mdi mdi-thermometer-lines" title="Apparent Temp" data-bind="visible: prefer_icons"></span><span class="secondary-info" data-bind="visible: !prefer_icons()">Apparent Temp:&nbsp;</span><span class="secondary-info" data-bind="html: apparent_temperature"></span><span class="secondary-info" data-bind="html: unit, attr: {style: sub_unit_style}"></span></p><p class="secondary-detail" data-bind="visible: humidity"><span class="secondary-icon mdi mdi-water-percent" title="Humidity" data-bind="visible: prefer_icons"></span><span class="secondary-info" data-bind="visible: !prefer_icons()">Humidity:&nbsp;</span><span class="secondary-info" data-bind="text: humidity"></span><span class="secondary-unit" data-bind="attr: {style: sub_unit_style}">%</span><br></p><p class="secondary-detail"  data-bind="visible: precip_probability() || precip_intensity()"><span data-bind="visible: precip_probability"><span class="secondary-icon mdi" title="Rain" data-bind="visible: prefer_icons, css: precip_type_icon"></span><span class="secondary-info" data-bind="visible: !prefer_icons()">Rain:&nbsp;</span><span class="secondary-info" data-bind="text: precip_probability"></span><span class="secondary-unit" data-bind="attr: {style: sub_unit_style}">%</span></span><span data-bind="visible: precip_intensity"><span class="secondary-info" data-bind="visible: precip_intensity() && precip_probability()">&nbsp;/&nbsp;</span><span class="secondary-info" data-bind="text: precip_intensity"></span><span class="secondary-unit" data-bind="text: rain_unit, attr: {style: sub_unit_style}"></span></span></p><p class="secondary-detail" data-bind="visible: wind_speed"><span class="secondary-icon mdi mdi-weather-windy" data-bind="visible: prefer_icons, css: bearing_icon, attr: {title: wind_bearing() + \'&deg;\'}"></span><span class="secondary-info" data-bind="visible: !prefer_icons()">Wind:&nbsp;</span><span class="secondary-info" data-bind="text: wind_speed"></span><span class="secondary-unit" data-bind="text: wind_unit, attr: {style: sub_unit_style}"></span></p><p class="secondary-detail" data-bind="visible: wind_bearing() && !prefer_icons()"><span class="secondary-info" data-bind="html: wind_bearing"></span><span class="secondary-unit" data-bind="attr: {style: sub_unit_style}">&deg;</span></p><p class="secondary-detail" data-bind="visible: pressure() != \'\'"><span class="secondary-icon mdi mdi-gauge" data-bind="visible: prefer_icons"></span><span class="secondary-info" data-bind="visible: !prefer_icons()">Pressure:&nbsp;</span><span class="secondary-info" data-bind="text: pressure"></span><span class="secondary-info" data-bind="text: pressure_unit, attr: {style: sub_unit_style}"></span></p><div data-bind="visible: show_forecast"> <hr><h1 class="title" data-bind="text: forecast_title, attr:{ style: title_style}, visible: show_forecast"></h1><p class="secondary-detail" data-bind="visible: forecast_temperature_min"><span class="secondary-climacon" data-bind="css: forecast_icon"></span></p><p class="secondary-detail" data-bind="visible: forecast_temperature_min"><span class="secondary-info" data-bind="text: forecast_temperature_min"></span><span class="secondary-info" data-bind="visible: forecast_temperature_max"><span>/</span><span class="secondary-info" data-bind="text: forecast_temperature_max"></span></span></p><p class="secondary-detail" data-bind="visible: forecast_precip_probability"><span class="secondary-icon mdi" title="Rain" data-bind="visible: prefer_icons, css: forecast_precip_type_icon"></span><span class="secondary-info" data-bind="visible: !prefer_icons()">Rain:&nbsp;</span><span class="secondary-info" data-bind="text: forecast_precip_probability"></span><span class="secondary-icon" data-bind="attr: {style: sub_unit_style}">%</span></p></div></div></div></li>', 3, 2, 1, 4)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-home" id="default-nav-home"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 1, 6)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-devices" id="default-nav-devices"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 2, 6)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-lights" id="default-nav-lights"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 3, 6)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-outside" id="default-nav-outside"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 1, 7)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-modes" id="default-nav-modes"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 2, 7)
    
    
    
    var widgets = {}
    // Initialize Widgets
    
        widgets["default-label"] = new basedisplay("default-label", "", "default", {'widget_type': 'basedisplay', 'fields': {'title': '', 'title2': '', 'value': 'Outside', 'unit': '', 'state_text': ''}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'unit_style': '', 'value_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #444;', 'container_style': ''}, 'css': {}, 'icons': [], 'static_icons': [], 'widget_style': 'background: #444;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1})
    
        widgets["default-sensor-front-yard-next-cycle"] = new basedisplay("default-sensor-front-yard-next-cycle", "", "default", {'widget_type': 'basedisplay', 'entity': 'sensor.front_yard_next_cycle', 'entity_to_sub_entity_attribute': '', 'sub_entity': '', 'sub_entity_to_entity_attribute': '', 'fields': {'title': '', 'title2': '', 'value': '', 'unit': '', 'state_text': ''}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;font-size: 100%;', 'widget_style': 'background-color: #444;background: #333;', 'container_style': ''}, 'css': {'value_style': 'color: #00aaff;font-size: 250%;', 'text_style': 'color: #fff;font-size: 100%;', 'unit_style': 'color: #00aaff;font-size: 100%;'}, 'icons': [], 'static_icons': [], 'title_is_friendly_name': 1, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-binary-sensor-front-yard-watering"] = new baseswitch("default-binary-sensor-front-yard-watering", "", "default", {'widget_type': 'baseswitch', 'entity': 'binary_sensor.front_yard_watering', 'state_active': 'on', 'state_inactive': 'off', 'fields': {'title': '', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fas-bullseye', 'icon_off': 'fas-minus'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #ff0055;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #333;'}, 'title_is_friendly_name': 1, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-switch-front-yard-manual-watering"] = new baseswitch("default-switch-front-yard-manual-watering", "", "default", {'widget_type': 'baseswitch', 'entity': 'switch.front_yard_manual_watering', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'switch.front_yard_manual_watering'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'switch.front_yard_manual_watering'}, 'fields': {'title': '', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fas-circle', 'icon_off': 'far-circle'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #333;'}, 'title_is_friendly_name': 1, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-sensor-pool-filler-next-cycle"] = new basedisplay("default-sensor-pool-filler-next-cycle", "", "default", {'widget_type': 'basedisplay', 'entity': 'sensor.pool_filler_next_cycle', 'entity_to_sub_entity_attribute': '', 'sub_entity': '', 'sub_entity_to_entity_attribute': '', 'fields': {'title': '', 'title2': '', 'value': '', 'unit': '', 'state_text': ''}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;font-size: 100%;', 'widget_style': 'background-color: #444;background: #333;', 'container_style': ''}, 'css': {'value_style': 'color: #00aaff;font-size: 250%;', 'text_style': 'color: #fff;font-size: 100%;', 'unit_style': 'color: #00aaff;font-size: 100%;'}, 'icons': [], 'static_icons': [], 'title_is_friendly_name': 1, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-binary-sensor-pool-filler-watering"] = new baseswitch("default-binary-sensor-pool-filler-watering", "", "default", {'widget_type': 'baseswitch', 'entity': 'binary_sensor.pool_filler_watering', 'state_active': 'on', 'state_inactive': 'off', 'fields': {'title': '', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fas-bullseye', 'icon_off': 'fas-minus'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #ff0055;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #333;'}, 'title_is_friendly_name': 1, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-switch-pool-filler-manual-watering"] = new baseswitch("default-switch-pool-filler-manual-watering", "", "default", {'widget_type': 'baseswitch', 'entity': 'switch.pool_filler_manual_watering', 'state_active': 'on', 'state_inactive': 'off', 'enable': 1, 'post_service_active': {'service': 'homeassistant/turn_on', 'entity_id': 'switch.pool_filler_manual_watering'}, 'post_service_inactive': {'service': 'homeassistant/turn_off', 'entity_id': 'switch.pool_filler_manual_watering'}, 'fields': {'title': '', 'title2': '', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fas-circle', 'icon_off': 'far-circle'}, 'static_icons': [], 'css': {'icon_style_active': 'color: #aaff00;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #333;'}, 'title_is_friendly_name': 1, 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-weather"] = new baseweather("default-weather", "", "default", {'widget_type': 'baseweather', 'fields': {'title': '', 'show_forecast': 0, 'prefer_icons': 0, 'unit': '', 'wind_unit': '', 'pressure_unit': '', 'rain_unit': '', 'temperature': '', 'humidity': '', 'precip_probability': '', 'precip_intensity': '', 'precip_type': '', 'wind_speed': '', 'pressure': '', 'wind_bearing': '', 'apparent_temperature': '', 'icon': '', 'bearing_icon': 'mdi-rotate-0', 'precip_type_icon': 'mdi-umbrella', 'forecast_title': '', 'forecast_temperature_min': '', 'forecast_temperature_max': '', 'forecast_icon': '', 'forecast_precip_probability': '', 'forecast_precip_type': '', 'forecast_precip_type_icon': 'mdi-umbrella'}, 'entities': {'icon': 'sensor.dark_sky_icon', 'temperature': 'sensor.dark_sky_temperature', 'apparent_temperature': 'sensor.dark_sky_apparent_temperature', 'humidity': 'sensor.dark_sky_humidity', 'precip_probability': 'sensor.dark_sky_precip_probability', 'precip_intensity': 'sensor.dark_sky_precip_intensity', 'precip_type': 'sensor.dark_sky_precip', 'pressure': 'sensor.dark_sky_pressure', 'wind_speed': 'sensor.dark_sky_wind_speed', 'wind_bearing': 'sensor.dark_sky_wind_bearing', 'forecast_icon': 'sensor.dark_sky_icon_1', 'forecast_temperature_min': 'sensor.dark_sky_daily_low_temperature_1', 'forecast_temperature_max': 'sensor.dark_sky_daily_high_temperature_1', 'forecast_precip_probability': 'sensor.dark_sky_precip_probability_1', 'forecast_precip_type': 'sensor.dark_sky_precip_1'}, 'css': {}, 'static_css': {'title_style': 'color: #00aaff;', 'unit_style': 'color: #ffaa00;', 'main_style': 'color: #ffaa00;', 'sub_style': 'color: #00aaff;', 'sub_unit_style': 'color: #00aaff;', 'widget_style': 'background-color: #444;background: #333;'}, 'icons': {'snow': 'mdi-snowflake', 'rain': 'mdi-umbrella', 'sleet': 'mdi-weather-snowy-rainy', 'unknown': 'mdi-umbrella'}, 'static_icons': [], 'units': '&deg;F', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
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
    ha_status(stream_url, "Outside", widgets);

});