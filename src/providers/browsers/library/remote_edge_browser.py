from selenium import webdriver
from selenium.webdriver.edge.options import Options
from src.providers.browsers.library.base_browser import BaseBrowser
from src.config.config import config


class RemoteEdgeBrowser(BaseBrowser):
    """Class for remote Edge."""

    @staticmethod
    def get_driver():
        """Return the driver for remote Edge."""
        options = Options()
        driver = webdriver.Remote(command_executor=config.SELENIUM_GRID_URL, options=options)

        return driver
