from typing import Any


class BaseProviderClass:
    def __getitem__(self, item_name: str) -> Any:
        """Raises exception when called if not overwritten by a child class (i.e. not implemented)."""
        raise NotImplementedError("__getitem__ is not implemented")
