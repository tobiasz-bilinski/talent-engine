from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from src.providers.browsers.library.base_browser import BaseBrowser


class ChromeBrowser(BaseBrowser):
    """Class for Chrome."""
    @staticmethod
    def get_driver():
        """Return the driver for Chrome."""
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        service_obj = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service_obj, options=options)
