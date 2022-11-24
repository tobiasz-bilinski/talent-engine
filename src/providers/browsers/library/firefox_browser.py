from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from src.providers.browsers.library.base_browser import BaseBrowser


class FirefoxBrowser(BaseBrowser):
    """Class for Firefox."""
    @staticmethod
    def get_driver():
        """Return the driver for Firefox."""
        service_obj = Service(GeckoDriverManager().install())
        return webdriver.Firefox(service=service_obj)
