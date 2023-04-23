from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100, default='')
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    weather_condition = models.CharField(max_length=100)
    wind_speed = models.FloatField()
    wind_gust = models.FloatField()
    wind_deg = models.FloatField()
    datetime = models.DateTimeField()
    timezone = models.FloatField()

    def __str__(self):        return self.name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for user information, such as name, age, address, etc.

class WeatherForecast(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    weather_condition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city.name} - {self.date}"