from typing import Any
from config_providers import OSConfigProvider, JSONConfigProvider


class Config:
    """Stores all the framework settings."""

    def __init__(self, config_providers):
        """Initializes instance, creates config dictionary, registers items."""
        self.config_providers = config_providers
        self.conf_dict = {}
        self._register("BASE_URL")
        self._register("SQL_CONNECTION_STRING")

    def get(self, item_name: str) -> Any:
        """Returns value of item_name stored in self.conf_dict."""
        return self.conf_dict[item_name]

    def _register(self, item_name):
        """
        Searches for item_name within the providers.
        If present: adds item_name and its value to conf_dict.
        Raises exception if item_name is not present in any provider.
        """
        for provider in self.config_providers:
            value = provider.get(item_name)
            if value is not None:
                self.conf_dict[item_name] = value
                return

        raise ValueError(f"{item_name} name is missing in config")


config = Config([OSConfigProvider, JSONConfigProvider])
print(config.get("SQL_CONNECTION_STRING"))
