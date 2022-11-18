import pytest
import time
from src.config.config import config
from src.models.user import User
from src.applications.weather_api import WeatherApi
from src.applications.URLS import URLS
from src.data.test_data import TestData


@pytest.fixture(scope="module")
def new_user_fixture():
    print("\nInitializing user")
    user = User(config.USERNAME, TestData.BIRTH_YEAR)
    yield user
    print("\nRemoving user")
    User.users.remove(user)


@pytest.fixture(scope="module")
def current_weather():
    weather_api = WeatherApi()
    res = weather_api.get_weather_data(
        URLS.weather, TestData.WEATHER_CORRECT_CITY)
    yield res
    del res


@pytest.fixture(scope="module")
def forecast():
    weather_api = WeatherApi()
    res = weather_api.get_weather_data(
        URLS.forecast, TestData.WEATHER_CORRECT_CITY)
    yield res
    del res


@pytest.fixture(scope="session", autouse=True)
def time_elapsed_fixture():
    time_start = time.time()
    yield
    time_elapsed = time.time() - time_start
    print(f"Time elapsed: {time_elapsed:.2f}s")
