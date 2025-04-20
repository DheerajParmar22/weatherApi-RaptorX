from django.urls import path
from .views import get_weather_by_ip

urlpatterns = [
    path('weather-by-ip', get_weather_by_ip, name='weather_by_ip'),
]
