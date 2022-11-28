from selenium.webdriver.common.by import By
from src.config.config import config


class ForgotPasswordPage:
    PAGE_URL = "/password_reset"
    email_field = (By.ID, "email_field")
<<<<<<< HEAD
<<<<<<< HEAD
    verification_button = (By.ID, "home_children_button")
=======
    verification_button = (By.CSS_SELECTOR, "#home_children_button")
>>>>>>> dc1e760 (Added page objects for login and forgot password pages.)
=======
>>>>>>> 1b42eb4 (Cosmetic changes)
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
<<<<<<< HEAD
<<<<<<< HEAD
        # Just an example, because it's a captcha so it doesn't make much sense
        # Also I'm not sure how to make Selenium wait for the button to appear
=======
>>>>>>> dc1e760 (Added page objects for login and forgot password pages.)
=======
>>>>>>> 1b42eb4 (Cosmetic changes)
        self.app.enter_text(self.email_field, email)

