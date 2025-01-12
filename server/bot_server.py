import time, json
from config.config import config
from libraryes import ntelegram
from handlers.msg_handler import MsgHandler

handler = MsgHandler()

class Server:
    def __init__(self):
        self.tg = ntelegram.telegram(config.telegram.token)
    
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

                if msg2 != "/start":
                    # debug
                    # print(answ.error)
                    answ = handler.exequte(msg2)
                    print(answ)
                    an = answ.answer
                    print(an)
                    if an != None and "error" not in str(an).lower():
                        self.tg.send("Вот ответ на ваше уравнение:\n\n" + an + "\n\nСпасибо, что используете нашего бота!")
                    elif answ.answer == "":
                        self.tg.send("Похоже, уравнение не имеет решения")
                    elif "error" in str(an).lower():
                        self.tg.send("Воникла ошибка при решении")
                    else:
                        self.tg.send("Похоже, возникла ошибка. В скором времени она будет исправлена")
                else:
                    self.tg.send("Hello")
            time.sleep(1)