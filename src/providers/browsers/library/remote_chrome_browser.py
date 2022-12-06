from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.providers.browsers.library.base_browser import BaseBrowser
from src.config.config import config


class RemoteChromeBrowser(BaseBrowser):
    """Class for remote Chrome."""

    @staticmethod
    def get_driver():
        """Return the driver for remote Chrome."""
        options = Options()
        driver = webdriver.Remote(command_executor=config.SELENIUM_GRID_URL, options=options)

        return driver
