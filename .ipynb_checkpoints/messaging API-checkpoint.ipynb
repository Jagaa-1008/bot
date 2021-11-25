{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: line-bot-sdk in /opt/anaconda3/lib/python3.7/site-packages (1.20.0)\n",
      "Requirement already satisfied: future in /opt/anaconda3/lib/python3.7/site-packages (from line-bot-sdk) (0.18.2)\n",
      "Requirement already satisfied: requests>=2.0 in /opt/anaconda3/lib/python3.7/site-packages (from line-bot-sdk) (2.22.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/anaconda3/lib/python3.7/site-packages (from requests>=2.0->line-bot-sdk) (2019.11.28)\n",
      "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /opt/anaconda3/lib/python3.7/site-packages (from requests>=2.0->line-bot-sdk) (1.25.8)\n",
      "Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /opt/anaconda3/lib/python3.7/site-packages (from requests>=2.0->line-bot-sdk) (3.0.4)\n",
      "Requirement already satisfied: idna<2.9,>=2.5 in /opt/anaconda3/lib/python3.7/site-packages (from requests>=2.0->line-bot-sdk) (2.8)\n",
      "\u001b[33mWARNING: You are using pip version 21.3; however, version 21.3.1 is available.\n",
      "You should consider upgrading via the '/opt/anaconda3/bin/python -m pip install --upgrade pip' command.\u001b[0m\n",
      "Requirement already satisfied: schedule in /opt/anaconda3/lib/python3.7/site-packages (1.1.0)\n",
      "\u001b[33mWARNING: You are using pip version 21.3; however, version 21.3.1 is available.\n",
      "You should consider upgrading via the '/opt/anaconda3/bin/python -m pip install --upgrade pip' command.\u001b[0m\n"
     ]
    }
   ],
   "source": [
    "!pip install line-bot-sdk\n",
    "!pip install schedule"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import tenki\n",
    "import schedule\n",
    "import time\n",
    "import os\n",
    "import contextlib, io\n",
    "\n",
    "file = open('info.json', 'r')\n",
    "info = json.load(file)\n",
    "from linebot import LineBotApi\n",
    "from linebot.models import TextSendMessage\n",
    "CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']\n",
    "line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)\n",
    "\n",
    "def houkoku():\n",
    "    USER_ID1 = info['USER_ID1']\n",
    "    USER_ID2 = info['USER_ID2']\n",
    "#    line_bot_api.push_message (USER_ID1, messages = TextSendMessage(text = txt))\n",
    "    line_bot_api.multicast ([USER_ID1, USER_ID2], messages = TextSendMessage(text = txt))\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    #tenki()\n",
    "    city = tenki.city\n",
    "    temp = str(tenki.temp)\n",
    "    desc = tenki.di\n",
    "    txt = \"%s \\ntemperature : %s \\n%s\" %(city,temp,desc)\n",
    "    #print(txt)\n",
    "    schedule.every().day.at(\"11:23\").do(houkoku)\n",
    "    while True:\n",
    "        schedule.run_pending()\n",
    "        time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
