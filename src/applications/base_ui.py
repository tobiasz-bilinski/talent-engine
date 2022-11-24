from typing import Any
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseUIApp:
    """Stores general helper functions for testing UI with Selenium."""

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_element(self, locator: tuple) -> Any:
        """Returns element with given locator.

        Args:
            locator (tuple): Stored in the page model (e.g. LoginPage.username_field). 

        Returns:
            Specified element.

        Raises:
            NoSuchElementException - if element can't be found.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))
        return element

    def click(self, locator: tuple) -> None:
        """Clicks on the element with specified locator.

        Args:
            locator (tuple): Stored in the page model (e.g. LoginPage.login_button).
        """
        element = self.get_element(locator)
        element.click()

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

    def close_window(self) -> None:
        self.driver.close()

    def quit_driver(self) -> None:
        self.driver.quit()
