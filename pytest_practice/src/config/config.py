from typing import Any
from config_providers import BaseProviderClass, OSConfigProvider, JSONConfigProvider


class Config:
    """Stores all the framework settings."""

    def __init__(self, config_providers):
        self.config_providers = config_providers
        self.conf_dict = {}
        self._register("BASE_URL")
        self._register("SQL_CONNECTION_STRING")

    def get(self, item_name: str) -> Any:
        return self.conf_dict[item_name]

    def _register(self, item_name):
        for provider in self.config_providers:
            value = provider.get(item_name)
            if value is not None:
                self.conf_dict[item_name] = value
                return

        raise ValueError(f"{item_name} name is missing in config")


config = Config([OSConfigProvider, JSONConfigProvider])
print(config.get("SQL_CONNECTION_STRING"))
