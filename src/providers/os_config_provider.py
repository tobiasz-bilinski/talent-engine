import os
from typing import Any
from src.providers.base_provider import BaseProviderClass


class OSConfigProvider(BaseProviderClass):
    def __getitem__(self, item_name: str) -> Any:
        """Returns value of environment variable item_name or None if it doesn't exist.
        
        Args:
            item_name (str): Item to get from configuration

        Returns:
            Any: Value of item in configuration
        """
        value = os.getenv(item_name)
        return value
