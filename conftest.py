import pytest
import time
from src.models.user import User
from src.applications.weather_api import WeatherApi
from src.data.URLS import URLS
from src.data.test_data import TestData
from src.applications.github_ui import GitHubUI


@pytest.fixture(scope="function")
def github_ui_fixture():
    github_ui_app = GitHubUI()
    github_ui_app.open_base_page()

    yield github_ui_app


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
    res = weather_api.get_weather_data(URLS.weather, TestData.WEATHER_CORRECT_CITY)
    yield res
    del res


@pytest.fixture(scope="module")
def forecast():
    """Yields JSON file for weather forecast data, converted to dict."""
    weather_api = WeatherApi()
    res = weather_api.get_weather_data(URLS.forecast, TestData.WEATHER_CORRECT_CITY)
    yield res
    del res


@pytest.fixture(scope="session", autouse=True)
def time_elapsed_fixture():
    """Prints out the time it took to run the tests."""
    time_start = time.time()
    yield
    time_elapsed = time.time() - time_start
    print(f"Time elapsed: {time_elapsed:.2f}s")
