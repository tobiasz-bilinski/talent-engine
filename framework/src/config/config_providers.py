import json
import os
from typing import Any


class BaseProviderClass:
    @staticmethod
    def get(item_name: str) -> Any:
        """Raises exception when called if not overwritten by a child class (i.e. not implemented)."""
        raise NotImplementedError("Not implemented")


class OSConfigProvider(BaseProviderClass):
    @staticmethod
    def get(item_name: str) -> Any:
        """Returns value of environment variable item_name or None if it doesn't exist."""
        value = os.getenv(item_name)
        return value


class JSONConfigProvider(BaseProviderClass):
    @staticmethod
    def _read_config(config_path):
        """Returns JSON object with contents of JSON file (path == config_path)."""
        with open(config_path) as json_file:
            return json.load(json_file)

    @staticmethod
    def get(item_name: str) -> Any:
        """Returns value of item_name in JSON object."""
        value = JSONConfigProvider._read_config(
            "/Users/perfectson/Documents/Testing/Talent Engine/talent-engine-2.0/pytest_practice/envs_configs/dev.json"
        )
        return value[item_name]
