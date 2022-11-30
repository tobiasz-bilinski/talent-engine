class BaseBrowser:
    @staticmethod
    def get_driver():
        """Raises exception if method is not implemented in child class."""
        raise NotImplementedError("Method not implemented.")
