import requests
import os

# api_key = os.environ.get('OPENWEATHERMAP_API_KEY')

def get_weather(lat, lon, API_KEY=os.environ.get('OPENWEATHERMAP_API_KEY')):
    """API Call"""

    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()