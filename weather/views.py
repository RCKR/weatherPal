from django.shortcuts import render
from .models import City
from .forms import CityForm
from .utils.weather import fetch_weather_data
from django.urls import reverse

ICON_MAPP = {
    "Clear": "fa-solid fa-sun",
    "Clouds": "fa-solid fa-cloud",
    "Atmosphere": "fa-solid fa-feather",
    "Snow": "fa-solid fa-snowflake",
    "Rain": "fa-solid fa-cloud-rain",
    "Drizzle": "fa-solid fa-cloud-sun-rain",
    "Thunderstorm": "fa-solid fa-cloud-bolt",
    "Extreme": "fa-solid fa-volcano",
    "Mist": "fa-solid fa-smog",
    "Smoke": "fa-solid fa-volcano",
    "Haze": "fa-solid fa-smog",
    "Dust": "fa-solid fa-smog",
    "Fog": "fa-solid fa-smog",
    "Sand": "fa-solid fa-meteor",
    "Ash": "fa-solid fa-volcano"
}


def weather(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['city']
            weather_data = fetch_weather_data(city_name)
            if weather_data:
                city = City(name=weather_data['city'],
                            country=weather_data['country'],
                            coordinates=weather_data['coordinates'],
                            temperature=weather_data['temperature'],
                            pressure=weather_data['pressure'],
                            humidity=weather_data['humidity'],
                            weather_condition=weather_data['weather_condition'],
                            wind_speed=weather_data['wind_speed'],
                            wind_gust=weather_data['wind_gust'] or -1,
                            wind_deg=weather_data['wind_deg'],
                            datetime=weather_data['dt'],
                            timezone=weather_data['tz'])
                city.save()
                weather_data['icon'] = ICON_MAPP[weather_data['main']]

                return render(request, 'weather/weather.html', {'form': form, 'city_data': weather_data})
            else:
                # Handle case when weather data is not available
                # You can render an error message or redirect to an error page
                pass
    else:
        form = CityForm()
        cities = City.objects.all()
        return render(request, 'weather/weather.html', {'form': form, 'cities': cities})
    

def renderHomePage(request):
    context = {
        'weather_url': reverse('weather')
    }
    return render(request, 'weather/index.html')
