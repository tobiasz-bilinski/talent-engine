import pytest
import time
from src.models.user import User
from src.applications.weather_api import WeatherApi
from src.data.URLS import URLS
from src.data.test_data import TestData
from src.applications.github_ui import GitHubUI
from src.providers.browsers.browsers_provider import BrowserProvider


@pytest.fixture(scope="function")
def github_enterprise(github_ui):
    """Open Enterprise Contact page, yield enterprise_contact_page object."""
    enterprise_contact_page = github_ui.enterprise_contact_page
    enterprise_contact_page.open_contact_page()
    yield enterprise_contact_page


@pytest.fixture(scope="function")
def github_about(github_ui):
    """Open About page, yield about_page object."""
    about_page = github_ui.about_page
    about_page.open_about_page()
    yield about_page


@pytest.fixture(scope="function")
def github_ui(request):
    """Sets up the driver and browser (if specified in CLI), opens base page."""
    browser = request.config.getoption("--browser")
    driver = BrowserProvider.get_driver(browser)
    github_ui_app = GitHubUI(driver)
    github_ui_app.open_base_page()
    yield github_ui_app
    github_ui_app.close_window()
    github_ui_app.quit_driver()


@pytest.fixture(scope="module")
def new_user_fixture():
    """Creates user object, then yields it and removes after tests are finished."""
    print("\nInitializing user")
    user = User(TestData.USERNAME, TestData.BIRTH_YEAR)
    yield user
    print("\nRemoving user")
    User.users.remove(user)


@pytest.fixture(scope="module")
def current_weather():
    """Yields JSON file for current weather data, converted to dict."""
    weather_api = WeatherApi()
    res = weather_api.get_weather_data(
        URLS.weather, TestData.WEATHER_CORRECT_CITY)
    yield res
    del res


@pytest.fixture(scope="module")
def forecast():
    """Yields JSON file for weather forecast data, converted to dict."""
    weather_api = WeatherApi()
    res = weather_api.get_weather_data(
        URLS.forecast, TestData.WEATHER_CORRECT_CITY)
    yield res
    del res


@pytest.fixture(scope="session", autouse=True)
def time_elapsed_fixture():
    """Prints out the time it took to run the tests."""
    time_start = time.time()
    yield
    time_elapsed = time.time() - time_start
    print(f"Time elapsed: {time_elapsed:.2f}s")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store",
                     choices=["chrome", "firefox", "edge"],
                     default="chrome",
                     help="Choose a browser to execute the tests with.")
