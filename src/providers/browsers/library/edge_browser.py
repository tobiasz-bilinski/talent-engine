from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from src.providers.browsers.library.base_browser import BaseBrowser


class EdgeBrowser(BaseBrowser):
    """Class for Microsoft Edge."""
    @staticmethod
    def get_driver():
        """Return the driver for Edge."""
        service_obj = Service(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service_obj)
