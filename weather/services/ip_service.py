import requests
from django.conf import settings
from dotenv import load_dotenv
import os

load_dotenv()

def get_location(ip):
    ipinfo_token = os.getenv('IPINFO_TOKEN')
    url = f'https://ipinfo.io/{ip}?token={ipinfo_token}'
    resp = requests.get(url, timeout=5)
    data = resp.json()
    return data['city'], data['country']
