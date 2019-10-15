"""
This component provides support for Home Automation Manager (HAM).
For more details about this component, please refer to the documentation at
https://home-assistant.io/components/ham/
"""
import logging

from .const import *

_LOGGER = logging.getLogger(__name__)


class HomeAutomationManagerConfigurationTransformer:
    def __init__(self, default_profile_parts, profiles, events, trackers, scenes):
        self._raw_default_profile_parts = default_profile_parts
        self._raw_profiles = profiles
        self._raw_events = events
        self._raw_scenes = scenes

        self._trackers = trackers
        self._profiles = {}
        self._scenes = {}
        self._events = {}
        self._custom_profiles = []
        self._configuration = {}
        self._configuration_errors = None

        self.build_configuration()

    def build_configuration(self):
        self.transform_profiles()
        self.transform_events()
        self.transform_scenes()

        self._configuration = {
            CONF_PROFILES: self._profiles,
            CONF_TRACKERS: self._trackers,
            CONF_SCENES: self._scenes,
            CONF_EVENTS: self._events,
            ATTR_CONFIG_ERRORS: self._configuration_errors,
            ATTR_CUSTOM_PROFILES: self._custom_profiles
        }

    def get_configuration(self):
        return self._configuration

    def log_warn(self, message):
        if self._configuration_errors is None:
            self._configuration_errors = []

        self._configuration_errors.append(f'WARN - {message}')
        _LOGGER.warning(message)

    def log_error(self, message):
        if self._configuration_errors is None:
            self._configuration_errors = []

        self._configuration_errors.append(f'ERROR - {message}')
        _LOGGER.error(message)

    def transform_profiles(self):
        try:
            if DEFAULT_PROFILE in self._raw_profiles:
                self.log_warn(f'{DEFAULT_PROFILE} profile is system profile')

            elif AWAY_PROFILE in self._raw_profiles:
                self.log_warn(f'{AWAY_PROFILE} profile is system profile')

            else:
                self.add_default_profiles()

                for profile in self._raw_profiles:
                    profile_name = profile[CONF_PROFILE_NAME]
                    parts = None

                    if CONF_PARTS in profile:
                        profile_parts = profile[CONF_PARTS]

                        parts = self.transform_profile_parts(profile_name, profile_parts)

                    self._profiles[profile_name] = {
                        CONF_PARTS: parts,
                        CONF_EVENTS: {}
                    }

                    if profile_name not in SYSTEM_PROFILES:
                        self._custom_profiles.append(profile_name)

        except Exception as ex:
            self.log_error(f'transform_profiles failed due to the following exception: {str(ex)}')

    def transform_profile_parts(self, profile_name, profile_parts):
        transformed_parts = {}

        try:
            if profile_parts is not None:
                for profile_part in profile_parts:
                    part_name = profile_part[CONF_NAME]
                    part_from = profile_part[CONF_PROFILE_FROM]

                    if part_name in transformed_parts:
                        self.log_warn(f'{profile_name} already contains part {part_name}')
                    else:
                        _LOGGER.info(f'Set part {profile_name} for profile {part_name} starting at: {part_from}')

                        transformed_parts[part_name] = part_from
        except Exception as ex:
            self.log_error(f'transform_profile_parts failed due to the following exception: {str(ex)}')

        return transformed_parts

    def transform_events(self):
        try:
            for event in self._raw_events:
                event_title = event[CONF_EVENT_TITLE]
                event_profile = event[CONF_PROFILE_NAME]
                event_date = None
                event_day = None

                if event_profile not in self._profiles:
                    self.log_warn(f'Cannot add event {event_title} since profile {event_profile} is undefined')
                elif event_profile in SYSTEM_PROFILES:
                    self.log_warn(f'Cannot add event {event_title} since profile {event_profile} is system profile')
                else:
                    event_date_time_key = None

                    if CONF_EVENT_DATE in event:
                        event_date = event[CONF_EVENT_DATE]
                        event_date_time_key = event_date

                    if CONF_EVENT_DAY in event:
                        event_day = event[CONF_EVENT_DAY]
                        event_date_time_key = event_day

                    event_id = f'{event_profile}.{event_title}.{event_date_time_key}'

                    events = self._profiles[event_profile][CONF_EVENTS]

                    _LOGGER.info(f'Adding event {event_title} at {event_date_time_key} for profile {event_profile}')

                    if event_date_time_key in self._events:
                        self._events[event_date_time_key].append({
                            CONF_PROFILE_NAME: event_profile,
                            CONF_EVENT_TITLE: event_title
                        })
                    else:
                        self._events[event_date_time_key] = [{
                            CONF_PROFILE_NAME: event_profile,
                            CONF_EVENT_TITLE: event_title
                        }]

                    if event_id in events:
                        self.log_warn(f'{event_profile} already contains event {event_title}')
                    else:
                        _LOGGER.info(f'Set event {event_profile} for profile {event_title}')

                        events[event_id] = {
                            CONF_EVENT_DAY: event_day,
                            CONF_EVENT_DATE: event_date,
                            CONF_EVENT_TITLE: event_title
                        }
        except Exception as ex:
            self.log_error(f'transform_events failed due to the following exception: {str(ex)}')

    def transform_scenes(self):
        try:
            for scene in self._raw_scenes:
                scene_name = scene[CONF_SCENE_NAME]
                scene_scripts = None

                if CONF_SCENE_SCRIPT in scene:
                    scene_scripts = scene[CONF_SCENE_SCRIPT]

                if scene_name not in SCENES_TYPES:
                    self.log_warn(f'Scene {scene_name} is not invalid')
                else:
                    _LOGGER.info(f'Set scene {scene_name}')

                    self._scenes[scene_name] = {
                        CONF_SCENE_NAME: scene_name,
                        CONF_SCENE_SCRIPT: scene_scripts
                    }
        except Exception as ex:
            self.log_error(f'transform_scenes failed due to the following exception: {str(ex)}')

    @staticmethod
    def get_key(prefix, suffix):
        key = f'{prefix}.{suffix}'

        return key

    def add_default_profiles(self):
        default_profile = {
            CONF_PROFILE_NAME: DEFAULT_PROFILE,
            CONF_PARTS: self._raw_default_profile_parts
        }

        away_profile = {
            CONF_PROFILE_NAME: AWAY_PROFILE
        }

        self._raw_profiles.append(default_profile)
        self._raw_profiles.append(away_profile)
