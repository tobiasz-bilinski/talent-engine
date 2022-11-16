from src.config.config import config


def test_city_in_correct_country_current_weather(weather_fixture_current):
    """Test if the country code for given city is correct. (For current weather)"""
    country = weather_fixture_current["sys"]["country"]

    assert country == config.WEATHER_CORRECT_COUNTRY


def test_current_weather_info_contains_data(weather_fixture_current):
    """Test if current weather info contains data (dict is not empty)."""

    assert len(weather_fixture_current["weather"][0]) is not 0


def test_city_in_correct_country_forecast(weather_fixture_forecast):
    """Test if the country code for given city is correct. (For forecast)"""
    country = weather_fixture_forecast["city"]["country"]

    assert country == config.WEATHER_CORRECT_COUNTRY


def test_forecast_length_is_correct(weather_fixture_forecast):
    """Test if forecast length is equal to expected."""

    assert weather_fixture_forecast["cnt"] == config.EXPECTED_FORECAST_LENGTH


def test_no_forecast_data_is_empty(weather_fixture_forecast):
    """Test if all objects in JSON response contain data."""
    for i in weather_fixture_forecast["list"]:
        if type(i) not in (list, dict):
            assert len(i) is not 0
        else:
            for j in i:
                assert len(j) is not 0
