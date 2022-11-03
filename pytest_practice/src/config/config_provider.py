import json
from typing import Any


class ConfigProvider:

    @staticmethod
    def _read_config(config_path):
        with open(config_path) as json_file:
            return json.load(json_file)

    @staticmethod
    def get(item_name: str) -> Any:
        value = ConfigProvider._read_config(
            "/home/tobiasz/talent-engine/pytest_practice/envs_configs/dev.json")
        return value[item_name]
