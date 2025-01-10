import time, json
from config.config import config
from libraryes import ntelegram
from handlers.msg_handler import MsgHandler

handler = MsgHandler()

class Server:
    def __init__(self):
        self.tg = ntelegram.telegram(config.tg_token)
    
    def serve(self):
        print("Bot is running...")

        while True:
            updates = self.tg.getUpdates(self.tg.cntUpd)
            # debug
            # print(self.tg.cntUpd)
            # debug
            # print(updates)

            if self.tg.cntUpd > self.tg.cntUpd_last:
                # debug
                #print(self.tg.cntUpd)
                msg = updates.get('result')[-1]
                # debug
                print(msg)
                msg1 = msg.get('message')
                # debug
                print(msg1)
                msg2 = msg1.get('text')
                # debug
                print(msg2)
                # debug
                # print(answ.error)
                answ = handler.exequte(msg)
                if answ.answer is not None:
                    self.tg.send("Вот ответ на ваше уравнение:\n\n" + answ.answer + "\n\nСпасибо, что используете нашего бота!")
                else:
                    self.tg.send("Похоже, возникла ошибка. В скором времени она будет исправлена")
            time.sleep(1)