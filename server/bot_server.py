import time, json
from config.config import config
from handlers.msg_handler import MsgHandler
from clients.qwen.qwen_client import QwenClient as q
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

handler = MsgHandler()

user_data = {}

class Server:
    # Функция обработки команд /start и /help
    async def start(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text('Привет! Отправь мне любое сообщение, и я отвечу тебе!')

    # Функция обработки текстовых сообщений
    async def send_message(self, update: Update, context: CallbackContext) -> None:
        # Отправляем обратно то же сообщение, что получил бот
        update.message.reply_text(f'Ты сказал: {update.message.text}')

    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """Обработка текстовых сообщений."""
        user_id = update.effective_user.id
        message = update.message.text

        if user_id not in user_data:
            user_data[user_id] = {"state": "start"}

        state = user_data[user_id]["state"]

        # Логика обработки сообщений
        if state == "start":
            if "привет" in message.lower():
                user_data[user_id]["state"] = "greeting"
                await update.message.reply_text("Привет! Чем могу помочь?")
            elif q.ask_question(data=message):
                user_data[user_id]["state"] = "equation"
            else:
                await update.message.reply_text("Напиши мне линейное, квадратное или рациоальное уравнение.")
        elif state == "greeting":
            if q.ask_question(data=message):
                user_data[user_id]["state"] = "equation"
            else:
                await update.message.reply_text("Рад снова Вас видеть!")
        elif state == "equation":
            await update.message.reply_text("Обрабатываю...")
            answer = handler.exequte(message)
            await update.message.reply_text(answer)
        else:
            await update.message.reply_text("Не понял Вас. Попробуйте переформулировать свой вопрос.")

    # Функция обработки ошибок
    async def error(self, update: Update, context: CallbackContext) -> None:
        print(f'Ошибка: {context.error}')

    async def run(self):
         # Создаем объект Application
        application = Application.builder().token(config.telegram.token).build()

        # Регистрируем обработчики команд и сообщений
        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

        # Запускаем бота
        await application.run_polling()
        
