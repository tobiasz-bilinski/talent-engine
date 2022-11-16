import pytest
import time
from src.config.config import config
from src.models.user import User
from src.applications.WeatherApi import WeatherApi
from src.applications.URLS import URLS


@pytest.fixture(scope="module")
def new_user_fixture():
    print("\nInitializing user")
    user = User(config.USERNAME, config.BIRTH_YEAR)
    yield user
    print("\nRemoving user")
    User.users.remove(user)


@pytest.fixture(scope="module")
def weather_fixture_current():
    weather_api = WeatherApi()
    res = weather_api.get_weather_data(
        URLS.weather, config.WEATHER_CORRECT_CITY)
    yield res
    del res


@pytest.fixture(scope="module")
def weather_fixture_forecast():
    weather_api = WeatherApi()
    res = weather_api.get_weather_data(
        URLS.forecast, config.WEATHER_CORRECT_CITY)
    yield res
    del res


@pytest.fixture(scope="session", autouse=True)
def time_elapsed_fixture():
    # Inspired by Kamil, it was just printing strings before and after yield but this is cooler :)
    time_start = time.time()
    yield
    time_elapsed = time.time() - time_start
    print(f"Time elapsed: {time_elapsed:.2f}s")
