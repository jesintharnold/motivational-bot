import json
import requests

class sarah_jesinth:



    def __init__(self):
        self.token=<token>
        self.base="https://api.telegram.org/bot"+self.token



    def get_update(self,offset=None):
        url="https://api.telegram.org/bot<tokenxxxxxxxxx>/getUpdates?timeout=100"
        if offset :
            url=url+"&offset={}".format(offset+1)
            r=requests.get(url)
            return json.loads(r.content)

    def send_message(self,msg,chat_id):
        url="https://api.telegram.org/bot<tokenxxxxxx>/sendMessage?text={}&chat_id={}".format(msg,chat_id)
        if msg is not None:
             requests.get(url)



