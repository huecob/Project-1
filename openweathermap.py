import requests
import os

def get_weather(lat, lon, openweather_api_key=os.environ.get('openweather_api_key')):
    """API Call"""

    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={openweather_api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None