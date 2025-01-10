import requests

##### Version 0.2
# 1) Change param channel_id
# 2) Add function channelId()
# 3) Add function getUpdates()


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