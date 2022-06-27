from datetime import datetime
import imp
from inspect import Parameter
from django.shortcuts import render
from django.http import HttpResponse
import json, urllib.request
import requests, datetime

def index(request):

    if request.method == 'POST':
        city = request.POST['city']
        URL = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=YOUR_API_KEY').read()
        list_of_data = json.loads(URL)
        data = {
            "name": str(list_of_data['name']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "feels_like": str(list_of_data['main']['feels_like']) + ' °C',
            "humidity": str(list_of_data['main']['humidity']) + ' %',
            "description": str(list_of_data['weather'][0]['description']),
        }
        print(data)
    else:
        data = {}

    return render(request, "index.html", data)
