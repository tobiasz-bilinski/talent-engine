from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from src.providers.browsers.library.base_browser import BaseBrowser


class ChromeBrowser(BaseBrowser):
    """Class for Chrome."""
    @staticmethod
    def get_driver():
        """Return the driver for Chrome."""
        service_obj = Service(ChromeDriverManager().install())
        return webdriver.Edge(service=service_obj)
