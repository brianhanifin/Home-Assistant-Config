import configparser
import os
import sys

import appdaemon.plugins.hass.hassapi as hass


class HassStatesLoad(hass.Hass):

    def initialize(self):

        self.listen_event(self.load_config, "plugin_started")
        self.listen_event(self.load_config, "appd_started")

    def create_config(self):
        self.log("No Config found, Creating new Config")
        config = configparser.ConfigParser()
        config.add_section("automation")
        config.add_section("boolean")
        config.add_section("datetime")
        config.add_section("number")
        config.add_section("select")
        config.add_section("text")
        config.add_section("tracker")
        with open(self.args["path"], "w") as config_file:
            config.write(config_file)
            config_file.close()

    def get_config(self):
        if not os.path.exists(self.args["path"]):
            self.create_config()
        config = configparser.ConfigParser()
        config.read(self.args["path"])
        return config

    def get_setting(self, section, setting):
        config = self.get_config()
        value = config.get(section, setting)
        return value

    def update_states(self, section, setting, value):
        if section == "automation":
            self.turn_off(setting)
        elif section == "boolean_on":
            self.turn_on(setting)
        elif section == "boolean_off":
            self.turn_off(setting)
        elif section == "datetime":
            self.call_service("input_datetime/set_datetime",
                              entity_id=setting, time=value)
        elif section == "number":
            self.set_value(setting, value)
        elif section == "select":
            self.select_option(setting, value)
        elif section == "text":
            self.call_service("input_text/set_value",
                              entity_id=setting, option=value)
        elif section == "tracker":
            self.call_service("device_tracker/see",
                              dev_id=setting.split(".")[1], location_name=value)

    def load_config(self, event_name, data, kwargs):
        config = self.get_config()
        for (setting, value) in config.items("automation"):
            if value == "off":
                self.update_states("automation", setting, value)
        for (setting, value) in config.items("boolean"):
            if self.get_state(setting) != value:
                if value == "on":
                    self.update_states("boolean_on", setting, value)
                else:
                    self.update_states("boolean_off", setting, value)
        for (setting, value) in config.items("datetime"):
            if self.get_state(setting) != value:
                self.update_states("datetime", setting, value)
        for (setting, value) in config.items("number"):
            if self.get_state(setting) != value:
                self.update_states("number", setting, value)
        for (setting, value) in config.items("select"):
            if self.get_state(setting) != value:
                self.update_states("select", setting, value)
        for (setting, value) in config.items("text"):
            if self.get_state(setting) != value:
                self.update_states("text", setting, value)
        for (setting, value) in config.items("tracker"):
            if self.get_state(setting) != value:
                self.update_states("tracker", setting, value)

        self.turn_on(self.args["isloaded_switch"])
        self.log("States Imported Successfully")