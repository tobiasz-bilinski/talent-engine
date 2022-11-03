import json
import os
from typing import Any


class BaseProviderClass:
    @staticmethod
    def get(item_name: str) -> Any:
        raise NotImplementedError("Not implemented")


class OSConfigProvider(BaseProviderClass):
    @staticmethod
    def get(item_name: str) -> Any:
        value = os.getenv(item_name)
        return value


class JSONConfigProvider(BaseProviderClass):
    @staticmethod
    def _read_config(config_path):
        with open(config_path) as json_file:
            return json.load(json_file)

    @staticmethod
    def get(item_name: str) -> Any:
        value = JSONConfigProvider._read_config(
            "/Users/perfectson/Documents/Testing/Talent Engine/talent-engine-2.0/pytest_practice/envs_configs/dev.json"
        )
        return value[item_name]
