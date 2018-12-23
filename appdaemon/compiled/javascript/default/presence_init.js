$(function(){ //DOM Ready

    function navigate(url)
    {
        window.location.href = url;
    }

    $(document).attr("title", "Presence");
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
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-presence-brian" id="default-presence-brian"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 1, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-baseswitch-default-presence-nerene" id="default-presence-nerene"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2><h1 class="state_text" data-bind="text: state_text, attr: {style: state_text_style}"></h1></div></li>', 1, 1, 2, 2)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-home" id="default-nav-home"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 1, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-devices" id="default-nav-devices"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 2, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-lights" id="default-nav-lights"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 3, 3)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-outside" id="default-nav-outside"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 1, 4)
    
        gridster.add_widget('<li><div data-bind="attr: {style: widget_style}" class="widget widget-basejavascript-default-nav-modes" id="default-nav-modes"><span class="toggle-area" id="switch"></span><h1 class="title" data-bind="text: title, attr:{style: title_style}"></h1><h1 class="title2" data-bind="text: title2, attr:{style: title2_style}"></h1><h2 class="icon" data-bind="attr:{style: icon_style}"><i data-bind="attr: {class: icon}"></i></h2></div></li>', 1, 1, 2, 4)
    
    
    
    var widgets = {}
    // Initialize Widgets
    
        widgets["default-label"] = new basedisplay("default-label", "", "default", {'widget_type': 'basedisplay', 'fields': {'title': '', 'title2': '', 'value': 'Presence', 'unit': '', 'state_text': ''}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'unit_style': '', 'value_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #444;', 'container_style': ''}, 'css': {}, 'icons': [], 'static_icons': [], 'widget_style': 'background: #444;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1})
    
        widgets["default-presence-brian"] = new baseswitch("default-presence-brian", "", "default", {'widget_type': 'baseswitch', 'entity': 'device_tracker.brian', 'state_active': 'on', 'state_inactive': 'off', 'fields': {'title': 'Brian', 'title2': 'Presence', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fa-male', 'icon_off': 'fa-male'}, 'static_icons': [], 'css': {'icon_style_active': 'color: lightblue;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #333;'}, 'icon_style_active': 'color: lightblue;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
        widgets["default-presence-nerene"] = new baseswitch("default-presence-nerene", "", "default", {'widget_type': 'baseswitch', 'entity': 'device_tracker.nerene', 'state_active': 'on', 'state_inactive': 'off', 'fields': {'title': 'Nerene', 'title2': 'Presence', 'icon': '', 'icon_style': '', 'state_text': ''}, 'icons': {'icon_on': 'fa-female', 'icon_off': 'fa-female'}, 'static_icons': [], 'css': {'icon_style_active': 'color: pink;', 'icon_style_inactive': 'color: #888;'}, 'static_css': {'title_style': 'color: #fff;', 'title2_style': 'color: #fff;', 'state_text_style': 'color: #fff;', 'widget_style': 'background-color: #444;background: #333;'}, 'icon_style_active': 'color: pink;', 'namespace': 'default', 'precision': 1, 'use_comma': 0, 'use_hass_icon': 1, 'widget_style': 'background: #333;'})
    
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
    ha_status(stream_url, "Presence", widgets);

});