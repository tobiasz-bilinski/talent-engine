from src.config.config import config
from src.applications.base_ui import BaseUIApp
from src.pages.login_page import LoginPage
from src.pages.forgot_password_page import ForgotPasswordPage
from src.pages.enterprise_contact_page import EnterpriseContactPage
from src.pages.about_page import AboutPage


class GitHubUI(BaseUIApp):
    """Stores helper functions for testing GitHub UI."""

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.login_page = LoginPage(self)
        self.forgot_password_page = ForgotPasswordPage(self)
        self.enterprise_contact_page = EnterpriseContactPage(self)
        self.about_page = AboutPage(self)

    def open_base_page(self) -> None:
        """Open base page."""
        self.open_page(config.BASE_URL_UI)

    def login(self, username: str, password: str) -> None:
        self.login_page.login(username, password)

    def logout(self) -> None:
        # TODO
        """Empty for now, because we're not logging in yet."""
        pass
