from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from src.config.config import config
from src.applications.base_ui import BaseUIApp
from src.models.login_page import LoginPage


class GitHubUI(BaseUIApp):

    def __init__(self):
        super().__init__()

    def open_base_page(self):
        self.open_page(config.BASE_URL_UI)

    def go_to_login_page(self):
        self.open_page(config.BASE_URL_UI + "/login")

    def login(self, username, password):
        self.enter_text(*LoginPage.username_field, username)
        self.enter_text(*LoginPage.password_field, password)
        self.click(*LoginPage.login_button)

    def logout(self):
        pass

    def check_title(self):
        return self.driver.title
