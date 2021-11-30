import json
#import tenki
import schedule
import time
import os
import contextlib, io
import requests

file = open('info.json', 'r')
info = json.load(file)
from linebot import LineBotApi
from linebot.models import TextSendMessage
CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def tenki():
    days = 7
    city_name = "Tokyo" 
    API_KEY = "80926725eda56fc4889304e886520e20"
    api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"

    url = api.format(city = city_name, cnt = days, key = API_KEY)
    
    response = requests.get(url)
    data = response.json()
    jsonText = json.dumps(data, indent=4)

    city = data['name']
    data1 = data['main']
    temp = data1['temp']
    data2 = data['weather'][0]
    di = data2['description']

def houkoku():
    USER_ID1 = info['USER_ID1']
    USER_ID2 = info['USER_ID2']
#    line_bot_api.push_message (USER_ID1, messages = TextSendMessage(text = txt))
    line_bot_api.multicast ([USER_ID1, USER_ID2], messages = TextSendMessage(text = txt))

if __name__ == '__main__':
    tenki()
    txt = "%s \ntemperature : %s \n%s" %(city,temp,di)
    houkoku()
