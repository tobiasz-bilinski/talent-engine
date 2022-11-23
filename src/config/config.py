"""Framework configuration module."""

from typing import Any
from src.providers.os_config_provider import OSConfigProvider
from src.providers.json_config_provider import JSONConfigProvider


class Config:
    """Stores all the framework settings."""

    def __init__(self, config_providers: list) -> None:
        """Initializes instance, creates config dictionary, registers items in config dictionary.

        Args:
            config_providers (list): List of providers that will be searched for items.
            Providers will be searched in given order.
        """
        self.config_providers = config_providers
        self.conf_dict = {}

        register_list = [
            "BASE_URL_API", "BASE_URL_UI",
            "USERNAME", "WEATHER_API_KEY", "SHARED_USERNAME", "SHARED_PASSWORD"
        ]
        for item in register_list:
            self._register(item)

    def __getattr__(self, item_name: str) -> Any:
        """Returns value of item_name stored in self.conf_dict, None if it's not present.

        Args:
            item_name (str): Previously registered item to be returned.

        Raises:
            AttributeError: Raised when item_name is not registered.

        Returns:
            Any: Value of item_name registered in self.conf_dict.
        """
        if item_name not in self.conf_dict:
            raise AttributeError("Variable not registered.")
        return self.conf_dict[item_name]

    def _register(self, item_name: str) -> None:
        """Searches for item_name within providers (in the given order). If it's
        present: adds item_name and its value to conf_dict.

        Args:
            item_name (str): Item to register from configuration providers.

        Raises:
            KeyError: Raised when item_name is not found in config providers.
        """
        for provider in self.config_providers:
            value = provider[item_name]
            if value is not None:
                self.conf_dict[item_name] = value
                return

        raise KeyError(f"{item_name} name not found in config providers.")


config = Config([JSONConfigProvider(), OSConfigProvider()])
