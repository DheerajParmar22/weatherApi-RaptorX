from django.test import TestCase
from weather.services.weather_service import get_weather

class WeatherServiceTest(TestCase):
    def test_weather_response_format(self):
        result = get_weather("Noida")
        self.assertIn("temperature", result)
        self.assertIn("humidity", result)
