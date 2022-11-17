import pytest
from requests.exceptions import HTTPError
from src.config.config import config
from src.applications.WeatherApi import WeatherApi
from src.applications.URLS import URLS


def test_city_in_correct_country_current_weather(weather_fixture_current):
    """Test if the country code for given city is correct. (For current weather)"""
    country = weather_fixture_current["sys"]["country"]

    assert country == WeatherApi.WEATHER_CORRECT_COUNTRY


def test_wrong_city_raises_exception_current_weather():
    """Test if passing a nonexistent city raises a HTTPError with status code 404."""
    with pytest.raises(HTTPError) as excinfo:
        weather_api = WeatherApi()
        res = weather_api.get_weather_data(
            URLS.weather, WeatherApi.WEATHER_WRONG_CITY)

    assert excinfo.type is HTTPError
    # Is it fine if this status code is hardcoded?
    assert "404" in excinfo.value.args[0]


def test_current_weather_info_contains_data(weather_fixture_current):
    """Test if current weather info contains data (dict is not empty)."""

    assert len(weather_fixture_current["weather"][0]) is not 0


def test_city_in_correct_country_forecast(weather_fixture_forecast):
    """Test if the country code for given city is correct. (For forecast)"""
    country = weather_fixture_forecast["city"]["country"]

    assert country == WeatherApi.WEATHER_CORRECT_COUNTRY


def test_forecast_length_is_correct(weather_fixture_forecast):
    """Test if forecast length is equal to expected."""

    assert weather_fixture_forecast["cnt"] == WeatherApi.EXPECTED_FORECAST_LENGTH


def test_no_forecast_data_is_empty(weather_fixture_forecast):
    """Test if all objects in JSON response contain data."""
    for i in weather_fixture_forecast["list"]:
        if type(i) not in (list, dict):
            assert len(i) is not 0
        else:
            for j in i:
                assert len(j) is not 0
