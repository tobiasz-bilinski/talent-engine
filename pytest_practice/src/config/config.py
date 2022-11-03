import json
import os
from typing import Any
# from src.config.config_provider import ConfigProvider


class Config:
    """Stores all the framework settings."""

    def __init__(self, config_providers):
        self.config_providers = config_providers
        self.conf_dict = {}
        self._register("BASE_URL")
        self._register("SQL_CONNECTION_STRING")
        self._register("SQL_CONNECTION_STRING2")

    def get(self, item_name: str) -> Any:
        return self.conf_dict[item_name]

    def _register(self, item_name):
        for provider in self.config_providers:
            value = provider.get(item_name)
            if value is not None:
                self.conf_dict[item_name] = value
                return

        raise ValueError(f"{item_name} name is missing in config")


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
            "/home/tobiasz/talent-engine/pytest_practice/envs_configs/dev.json")
        return value[item_name]


config = Config([OSConfigProvider, JSONConfigProvider])
print(config.get['SQL_CONNECTION_STRING'])
