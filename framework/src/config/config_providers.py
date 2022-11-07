import json
import os


class BaseProviderClass:
    @staticmethod
    def get(item_name):
        """Raises exception when called if not overwritten by a child class (i.e. not implemented)."""
        raise NotImplementedError("Not implemented")


class OSConfigProvider(BaseProviderClass):
    @staticmethod
    def get(item_name):
        """Returns value of environment variable item_name or None if it doesn't exist."""
        value = os.getenv(item_name)
        return value


class JSONConfigProvider(BaseProviderClass):
    @staticmethod
    def _read_config(config_path):
        """Returns a dictionary with the contents of JSON file (path == config_path)."""
        with open(config_path) as json_file:
            return json.load(json_file)

    @staticmethod
    def get(item_name):
        """Returns value of item_name in dictionary received from _read_config."""
        value = JSONConfigProvider._read_config(
            "/Users/perfectson/Documents/Testing/Talent Engine/talent-engine-2.0/framework/envs_configs/dev.json"
        )
        return value[item_name]
