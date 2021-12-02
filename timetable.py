import json
file = open('timetable.json','r')
info = json.load(file)
jsonText = json.dumps(info, indent=4, ensure_ascii=False)

monday = json.dumps(info['Monday'], indent=4, ensure_ascii=False)
tuesday = json.dumps(info['Tuesday'], indent=4, ensure_ascii=False)
wednesday = json.dumps(info['Wednesday'], indent=4, ensure_ascii=False)
thursday = json.dumps(info['Thursday'], indent=4, ensure_ascii=False)
friday = json.dumps(info['Friday'], indent=4, ensure_ascii=False)

from datetime import date
import calendar
curr_date = date.today()
today = calendar.day_name[curr_date.weekday()]

from linebot import LineBotApi
from linebot.models import TextSendMessage
file1 = open('info.json', 'r')
info1 = json.load(file1)
CHANNEL_ACCESS_TOKEN = info1['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID1 = info1['USER_ID1']
    USER_ID2 = info1['USER_ID2']
    if (today == 'Monday'):
        messages = monday
    elif (today == 'Tuesday'):
        messages = tuesday
    elif (today == 'Wednesday'):
        messages = wednesday
    elif (today == 'Thursday'):
        messages = thursday
    elif (today == 'Friday'):
        messages = friday
    elif (today == 'Saturday'):
        messages = saturday
    elif (today == 'Sunday'):
        messages = sunday
    
    line_bot_api.push_message (USER_ID1, messages = TextSendMessage(messages))
    
if __name__ == '__main__':
    main()


