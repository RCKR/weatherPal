from django.urls import path
from .views import weather, renderHomePage

urlpatterns = [
    path('weather/', weather, name='weather'),
    path('', renderHomePage, name='home_page')
]