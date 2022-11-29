from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from src.providers.browsers.library.base_browser import BaseBrowser


class FirefoxBrowser(BaseBrowser):
    """Class for Firefox."""
    @staticmethod
    def get_driver():
        """Return the driver for Firefox."""
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        service_obj = Service(GeckoDriverManager().install())
        return webdriver.Firefox(service=service_obj, options=options)
