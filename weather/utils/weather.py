import requests
from config import WEATHER_API_KEY

def fetch_weather_data(city_name: str) -> dict:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        # Handle successful response
        weather_data = response.json()
        # Extract relevant information from the weather_data JSON
        weather = {
            'city': weather_data['name'],
            'country': weather_data['sys']['country'],
            'coordinates': ';'.join(str(v) for v in weather_data['coord'].values()),
            'temperature': weather_data['main']['temp'],
            'pressure': weather_data['main']['pressure'],
            'humidity': weather_data['main']['humidity'],
            'weather_condition': weather_data['weather'][0]['description'],
            'main': weather_data['weather'][0]['main'],
            'wind_speed': weather_data['wind']['speed'],
            'wind_gust': weather_data['wind'].get('gust'),
            'wind_deg': weather_data['wind']['deg'],
            'dt': weather_data['dt'],
            'tz': weather_data['timezone']
        }
        return weather
    else:
        # Handle error response
        print('Failed to fetch weather data:', response.text)
        return None
    

def fetch_weather_forecast(city_name, forecast_duration):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={WEATHER_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        # Handle successful response
        forecast_data = response.json()
        # Extract relevant information from the forecast_data JSON
        forecast = []
        for forecast_item in forecast_data['list'][:forecast_duration]:
            weather = {
                'datetime': forecast_item['dt_txt'],
                'temperature': forecast_item['main']['temp'],
                'description': forecast_item['weather'][0]['description'],
            }
            forecast.append(weather)
        return forecast
    else:
        # Handle error response
        print('Failed to fetch weather forecast data:', response.text)
        return None


