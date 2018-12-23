import configparser
import os
import sys
import threading

import appdaemon.plugins.hass.hassapi as hass


class HassStatesSave(hass.Hass):

    def initialize(self):

        self.lock = threading.Lock()
        self.listen_state(self.save_config, "automation")
        self.listen_state(self.save_config, "input_boolean")
        self.listen_state(self.save_config, "input_datetime")
        self.listen_state(self.save_config, "input_number")
        self.listen_state(self.save_config, "input_select")
        self.listen_state(self.save_config, "input_text")
        self.listen_state(self.save_config, "device_tracker")

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

    def save_config(self, entity, attribute, old, new, kwargs):
        self.lock.acquire()
        try:
            if new != old:
                # device = self.friendly_name(entity)
                if entity != self.args["isloaded_switch"]:
                    section = entity.split(".")[0]
                    if section != "automation":
                        section = section.split("_")[1]
                    config = self.get_config()
                    config.set(section, entity, new)
                    with open(self.args["path"], "w") as config_file:
                        config.write(config_file)
                        config_file.close()
                        # message = "{} state saved as {}".format(device, new)
                        # self.log(message)
        finally:
            self.lock.release()