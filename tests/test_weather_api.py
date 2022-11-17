import pytest
from requests.exceptions import HTTPError
from src.config.config import config
from src.data.test_data import TestData
from src.applications.URLS import URLS
from src.applications.weather_api import WeatherApi
from helpers import validate_json


def test_city_in_correct_country_current_weather(current_weather):
    """Test if the country code for given city is correct. (For current weather)"""
    country = current_weather["sys"]["country"]

    assert country == TestData.WEATHER_CORRECT_COUNTRY


def test_wrong_city_raises_exception_current_weather():
    """Test if passing a nonexistent city raises a HTTPError with status code 404."""
    with pytest.raises(HTTPError) as excinfo:
        weather_api = WeatherApi()
        res = weather_api.get_weather_data(
            URLS.weather, TestData.WEATHER_WRONG_CITY)

    assert excinfo.value.response.status_code == 404


def test_city_in_correct_country_forecast(forecast):
    """Test if the country code for given city is correct. (For forecast)"""
    country = forecast["city"]["country"]

    assert country == TestData.WEATHER_CORRECT_COUNTRY


def test_forecast_length_is_correct(forecast):
    """Test if forecast length is equal to expected."""

    assert forecast["cnt"] == TestData.EXPECTED_FORECAST_LENGTH


def test_validate_json_schema_current_weather(current_weather):
    """Test if JSON schema in response is correct."""
    # TODO: JSON SCHEMA VALIDATION
    assert validate_json(current_weather)
