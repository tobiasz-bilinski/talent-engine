from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from src.providers.browsers.library.base_browser import BaseBrowser
from src.config.config import config


class RemoteFirefoxBrowser(BaseBrowser):
    """Class for remote Firefox."""

    @staticmethod
    def get_driver():
        """Return the driver for remote Firefox."""
        options = Options()
        driver = webdriver.Remote(command_executor=config.SELENIUM_GRID_URL, options=options)

        return driver
