from django.http import JsonResponse
from .services.ip_service import get_location
from .services.weather_service import get_weather
from .utils.validators import validate_ip
import logging

logger = logging.getLogger(__name__)

def get_weather_by_ip(request):
    ip = request.GET.get('ip') or request.META.get('REMOTE_ADDR')
    
    if not validate_ip(ip):
        return JsonResponse({'error': 'Invalid IP address'}, status=400)

    try:
        city, country = get_location(ip)
        weather_data, status = get_weather(city)

        if status != 200:
            return JsonResponse(weather_data, status=status)

        return JsonResponse({
            'ip': ip,
            'location': {'city': city, 'country': country},
            'weather': weather_data
        })

    except Exception as e:
        logger.error(f"Error fetching weather for IP {ip}: {str(e)}")
        return JsonResponse({'error': 'Unable to fetch weather'}, status=500)
