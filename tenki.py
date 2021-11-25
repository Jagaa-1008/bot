#!/usr/bin/env python
# coding: utf-8
import requests
import json
#import urllib
# import numpy as np
def tenki():
    days = 7
    city_name = "Tokyo" 
    API_KEY = "80926725eda56fc4889304e886520e20"
    api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"
    #api = "http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={cnt}&appid={key}"

    url = api.format(city = city_name, cnt = days, key = API_KEY)
    #print(url)
    response = requests.get(url)
    data = response.json()
    jsonText = json.dumps(data, indent=4)
    #print(jsonText)

    city = data['name']
    data1 = data['main']
    temp = data1['temp']
    data2 = data['weather'][0]
    di = data2['description']
#print(city)
#print(temp)
#print(di)

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    tenki()


