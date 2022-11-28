from selenium.webdriver.common.by import By
from src.config.config import config


class ForgotPasswordPage:
    PAGE_URL = "/password_reset"
    email_field = (By.ID, "email_field")
    submit_button = (By.NAME, "commit")

    def __init__(self, app):
        self.app = app

    def open_forgot_password_page(self):
        self.app.open_page(config.BASE_URL_UI + self.PAGE_URL)

    def fill_email(self, email):
        """Fill out email field.

        Args:
            email (str): Shared email stored in config.

        """
        self.app.enter_text(self.email_field, email)

