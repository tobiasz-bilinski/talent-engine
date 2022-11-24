import json
from typing import Any
from src.providers.base_provider import BaseProviderClass


class JSONConfigProvider(BaseProviderClass):
    @staticmethod
    def _read_config(config_path: str) -> dict:
        """Returns a dictionary with the contents of JSON file.

        Args:
            config_path (str): Absolute path to JSON config file.

        Returns:
            Dictionary with the contents of JSON file.
        """
        with open(config_path) as json_file:
            return json.load(json_file)

    def __getitem__(self, item_name: str) -> Any:
        """Returns value of item_name in dictionary returned by _read_config.

        Args:
            item_name (str): Item to get from the dictionary returned by _read_config.

        Returns:
            Value of item_name in dictionary returned by _read_config.
        """
        value = JSONConfigProvider._read_config(
            "/home/tobiasz/talent-engine/envs_configs/dev.json"
        )
        return value.get(item_name)
