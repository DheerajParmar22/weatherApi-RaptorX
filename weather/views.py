# from django.shortcuts import render
# from django.http import JsonResponse
# from .services.ip_service import get_location
# from .services.weather_service import get_weather
# from .utils.validators import validate_ip
# import logging
# logger = logging.getLogger(__name__)
# # from ratelimit.decorators import ratelimit
# # from ratelimit import ratelimit




# # @ratelimit(key='ip', rate='5/m', block=True)
# def get_weather_by_ip(request):
#     ip = request.GET.get('ip') or request.META.get('REMOTE_ADDR')
    
#     if not validate_ip(ip):
#         return JsonResponse({'error': 'Invalid IP address'}, status=400)

#     try:
#         city, country = get_location(ip)
#         weather_data = get_weather(city)
#         print(weather_data)
#         # if weather_data.error and weather_data.error == 'Rate limit exceeded':
#         #     return JsonResponse({'error': 'Rate limit exceeded'}, status=429)
        
#         return JsonResponse({
#             'ip': ip,
#             'location': {'city': city, 'country': country},
#             'weather': weather_data
#         })

#     except Exception as e:
#         logger.error(f"Error fetching weather for IP {ip}: {str(e)}")
#         return JsonResponse({'error': 'Unable to fetch weather'}, status=500)



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
