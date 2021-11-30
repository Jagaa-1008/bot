import json
import tenki
import schedule
import time
import os
import contextlib, io

file = open('info.json', 'r')
info = json.load(file)
from linebot import LineBotApi
from linebot.models import TextSendMessage
CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def houkoku():
    USER_ID1 = info['USER_ID1']
    USER_ID2 = info['USER_ID2']
#    line_bot_api.push_message (USER_ID1, messages = TextSendMessage(text = txt))
    line_bot_api.multicast ([USER_ID1, USER_ID2], messages = TextSendMessage(text = txt))

if __name__ == '__main__':
    city = tenki.city
    temp = str(tenki.temp)
    desc = tenki.di
    txt = "%s \ntemperature : %s \n%s" %(city,temp,desc)
    houkoku()