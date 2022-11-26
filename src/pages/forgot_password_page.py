from selenium.webdriver.common.by import By
from src.config.config import config


class ForgotPasswordPage:
    PAGE_URL = "/password_reset"
    email_field = (By.ID, "email_field")
    verification_button = (By.ID, "home_children_button")
    submit_button = (By.NAME, "commit")

    def __init__(self, app):
        self.app = app

    def open_forgot_password_page(self):
        self.app.open_page(config.BASE_URL_UI + self.PAGE_URL)

    def fill_and_submit(self, email):
        """Fill out email field, click verify button, click submit button.

        Args:
            email (str): Shared email stored in config.

        """
        # Just an example, because it's a captcha so it doesn't make much sense
        # Also I'm not sure how to make Selenium wait for the button to appear
        self.app.enter_text(self.email_field, email)
        self.app.click(self.verification_button)
        self.app.click(self.submit_button)

