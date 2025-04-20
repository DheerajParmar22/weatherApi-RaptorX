# import requests
# from django.core.cache import cache
# from django.http import JsonResponse
# from django.conf import settings
# from dotenv import load_dotenv
# import os

# load_dotenv()

# RATE_LIMIT = 10

# def get_weather(city):

#     rate_limit_key = f"rate_limit_{city.lower()}"
#     request_count = cache.get(rate_limit_key)
#     print(request_count)

#     if request_count:
#         cache.incr(rate_limit_key)
#     else:
#         cache.set(rate_limit_key, 1, timeout=600)

#     if request_count and request_count >= RATE_LIMIT:
#         return {"error": "Rate limit exceeded"}

#     cache_key = f"weather_{city.lower()}"
#     cached_data = cache.get(cache_key)
    
#     if cached_data:
#         return cached_data

#     openweather_key = os.getenv('OPENWEATHER_API_KEY')
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_key}&units=metric"
#     resp = requests.get(url, timeout=5)
#     data = resp.json()
#     print("not returned from cache only..........")
#     result = {
#         "temperature": data['main']['temp'],
#         "humidity": data['main']['humidity'],
#         "description": data['weather'][0]['description']
#     }

#     cache.set(cache_key, result, timeout=600) 

#     return result



import requests
from django.core.cache import cache
from dotenv import load_dotenv
import os

load_dotenv()

RATE_LIMIT = 10

def get_weather(city):
    rate_limit_key = f"rate_limit_{city.lower()}"
    request_count = cache.get(rate_limit_key)

    if request_count:
        cache.incr(rate_limit_key)
    else:
        cache.set(rate_limit_key, 1, timeout=600)

    if request_count and request_count >= RATE_LIMIT:
        return {"error": "Rate limit exceeded"}, 429

    cache_key = f"weather_{city.lower()}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return cached_data, 200

    openweather_key = os.getenv('OPENWEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_key}&units=metric"
    
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        result = {
            "temperature": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "description": data['weather'][0]['description']
        }

        cache.set(cache_key, result, timeout=600)
        return result, 200

    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch weather data: {str(e)}"}, 500
