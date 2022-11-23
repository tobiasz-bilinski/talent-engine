import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException


class BaseUIApp:

    def __init__(self):
        service_obj = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service_obj)
        self.driver.implicitly_wait(5)

    def get_element(self, locator_type, locator_value):
        return self.driver.find_element(locator_type, locator_value)

    def click(self, locator_type, locator_value):
        el = self.get_element(locator_type, locator_value)
        el.click()

    def enter_text(self, locator_type, locator_value, text):
        el = self.get_element(locator_type, locator_value)
        el.send_keys(text)

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
