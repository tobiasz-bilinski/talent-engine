from src.config.config import config
from src.applications.base_ui import BaseUIApp
from src.models.login_page import LoginPage
from src.data.URLS import URLS


class GitHubUI(BaseUIApp):
    """Stores helper functions for testing GitHub UI."""

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open_base_page(self) -> None:
        """Open base page."""
        self.open_page(config.BASE_URL_UI)

    def go_to_login_page(self) -> None:
        """Go to login page."""
        self.open_page(config.BASE_URL_UI + URLS.github_login)

    def login(self, username: str, password: str) -> None:
        """Fill out username and password fields, click login button.

        Args:
            username (str): Shared username stored in config.
            password (str): Shared password stored in config.

        """
        self.enter_text(LoginPage.username_field, username)
        self.enter_text(LoginPage.password_field, password)
        self.click(LoginPage.login_button)

    def logout(self) -> None:
        # TODO
        """Empty for now, because we're not logging in yet."""
        pass

    def get_title(self) -> str:
        """Return page title."""
        return self.driver.title
