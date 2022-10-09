import os
import json
import requests
from dotenv import load_dotenv

import utils
import db

load_dotenv()
# tokenとsecretを貼り付ける
token = os.getenv("TOKEN") # copy and paste from the SwitchBot app V6.14 or later
secret = os.getenv("secret") # copy and paste from the SwitchBot app V6.14 or later
headers = utils.make_request_header(token,secret)

def scan(deviceId):
    # url: https://api.switch-bot.com/v1.1/devices/xxxxxxxx/status
    url = os.getenv("v1.1_url") + "devices/" + deviceId + "/status"
    try:
        # APIでデバイスの取得を試みる
        res = requests.get(url, headers=headers)
        res.raise_for_status()

        print(res.text)

    except requests.exceptions.RequestException as e:
        print('response error:',e)
    

if __name__ =="__main__":
    scan()