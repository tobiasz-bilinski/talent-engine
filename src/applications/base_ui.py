from typing import Any
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BaseUIApp:
    """Stores general helper functions for testing UI with Selenium."""

    def __init__(self) -> None:
        """Initialize service object and driver, tell driver to implicitly wait for elements etc."""
        service_obj = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service_obj)
        self.driver.implicitly_wait(5)

    def get_element(self, locator: tuple) -> Any:
        """Get element with given locator.
        
        Args:
            locator (tuple): Stored in the page model (e.g. LoginPage.username_field). 
        
        Returns:
            Specified element.

        Raises:
            NoSuchElementException - if element can't be found.
        """

        return self.driver.find_element(*locator)

    def click(self, locator: tuple) -> None:
        """Clicks on the element with specified locator.
        
        Args:
            locator (tuple): Stored in the page model (e.g. LoginPage.login_button).
        """
        el = self.get_element(locator)
        el.click()

    def enter_text(self, locator: tuple, text: str) -> None:
        """Sends specified text to element with given locator.
        
        Args:
            locator (tuple): Stored in the page model (e.g. LoginPage.username_field).
            text (str): Text to be sent to the element.
        
        """
        el = self.get_element(locator)
        el.send_keys(text)

    def open_page(self, url: str) -> None:
        """Opens page with specified url."""
        self.driver.get(url)
        self.driver.maximize_window()
