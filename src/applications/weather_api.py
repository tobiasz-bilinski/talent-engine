import requests
from urllib.parse import urljoin
from src.config.config import config


class WeatherApi:
    """Class for communicating with OpenWeather API."""

    def __init__(self) -> None:
        pass

    def _form_url(self, base_url, url) -> str:
        """Combine URL from parts."""
        return urljoin(base_url, url)

    def get_weather_data(self, current_or_forecast: str, city_name: str) -> dict:
        """Return weather data in JSON converted to dict.

        Args:
            current_or_forecast (str): URL stored in URLS module (URLS.weather or URLS.forecast).        
            city_name(str): Name of the city (passed from within tests).

        Returns:
            dict: Dictionary with weather data.
        """

        url = self._form_url(config.BASE_URL_API, current_or_forecast)
        params = {"q": city_name, "appid": config.WEATHER_API_KEY}

        r = requests.get(url=url, params=params)
        r.raise_for_status()
        return r.json()
