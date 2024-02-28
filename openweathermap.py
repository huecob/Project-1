import requests
import os
from geopy.geocoders import Nominatim

def get_weather(lat, lon, openweather_api_key=os.environ.get('openweather_api_key')):
    """API Call"""

    url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourly,daily&appid={openweather_api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None
    
def get_city(latitude, longitude):

    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    address = location.address
    # Extract city from address
    city = address.split(",")[-3]
    return city.strip()
