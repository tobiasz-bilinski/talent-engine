from selenium.webdriver.common.by import By
from src.config.config import config


class LoginPage:
    PAGE_URL = "/login"
    username_field = (By.ID, "login_field")
    password_field = (By.ID, "password")
    login_button = (By.NAME, "commit")

    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        self.app.open_page(config.BASE_URL_UI + self.PAGE_URL)

    def login(self, username, password):
        """Fill out username and password fields, click login button.

        Args:
            username (str): Shared username stored in config.
            password (str): Shared password stored in config.

        """
        self.app.enter_text(self.username_field, username)
        self.app.enter_text(self.password_field, password)
        self.app.click(self.login_button)

