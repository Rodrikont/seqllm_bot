
import requests

##### Version 0.2
# 1) Change param channel_id
# 2) Add function channelId()
# 3) Add function getUpdates()

##### Version 0.1

TG_T_NFINANCE = "2121334788:AAFHILjHrD_rebyjDM9MvnT1fOV-TYPd8sQ"
TG_CH_ID_NFINANCE = "475133928"

TG_T_NEOSYNAS = "1181297154:AAEg0XR_8q7r0mDIolAjoZI79ox1w6X2NA0"
TG_CH_ID_NEOSYNAS = "475133928"

class telegram:
    def __init__(self, token, channel_id = None):
        self.token = token
        self.channel_id = channel_id
        self.url = "https://api.telegram.org/bot"
        self.c_sendMessage = "sendMessage"
        self.c_getUpdates = "getUpdates"
        self.updates = None
        self.cntUpd = 0
        self.cntUpd_last = None

    def channelId(self, channel_id = None):
        if channel_id != None :
            self.channel_id = channel_id
        return self.channel_id

    def send(self, text: str, channel_id = None):
        url = self.url + self.token + "/" + self.c_sendMessage
        ch_id = self.channel_id if channel_id == None else channel_id

        if ch_id == None:
            raise Exception("param 'channel_id' is not defined")

        r = requests.post(url, data={
             "chat_id": ch_id,
             "text": text
              })

        if r.status_code != 200:
            raise Exception("post_text error")

    def getUpdates(self, b):
        url = self.url + self.token + "/" + self.c_getUpdates
        r = requests.post(url)

        if r.status_code != 200:
            raise Exception("post_text error")

        self.updates = r.json()
        cnt = len(self.updates["result"])
        if self.cntUpd_last == None:
            self.cntUpd_last = cnt
        else:
            self.cntUpd_last = self.cntUpd
        if b != cnt:
            a = self.updates.get('result')[cnt - 1].get('message').get('from').get('id')
            self.channel_id = a
        self.cntUpd = cnt

        return self.updates
'''

import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

class telegram:
    def __init__(self, token):
        self.token = token
        self.channel_id = self.start()
        self.c_getUpdates = "getUpdates"
        self.cntUpd = 0
        self.cntUpd_last = None
        self.url = "https://api.telegram.org/bot"
    
    def start(self, update: Update, context: CallbackContext) -> None:
        return update.effective_chat.id

    def send(self, text: str):
        url = self.url + self.token
        method = url + "/sendMessage"

        r = requests.post(method, data={
             "chat_id": self.channel_id,
             "text": text
              })

        if r.status_code != 200:
            raise Exception("post_text error")
        
    def getUpdates(self):
        url = self.url + self.token + "/" + self.c_getUpdates
        r = requests.post(url)

        if r.status_code != 200:
            raise Exception("post_text error")

        self.updates = r.json()
        cnt = len(self.updates["result"])
        if self.cntUpd_last == None:
            self.cntUpd_last = cnt
        else:
            self.cntUpd_last = self.cntUpd
        self.cntUpd = cnt

        return self.updates
'''