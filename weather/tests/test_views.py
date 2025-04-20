from django.test import Client, TestCase

class WeatherByIPTest(TestCase):
    def test_invalid_ip(self):
        c = Client()
        response = c.get('/weather-by-ip?ip=999.999.999.999')
        self.assertEqual(response.status_code, 400)
