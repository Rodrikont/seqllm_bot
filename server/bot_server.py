from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from usecases.solver_usecase import SolverUsecase
from enums.status_enums import Status
from config.config import config

uscase = SolverUsecase()
user_data = {}

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я могу решить уравненние.\nКакое уравнение тебе решить?")

# Обработчик текстовых сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    await update.message.reply_text(f"Ты написал: {user_message}")

# Обработчик текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка текстовых сообщений."""
    user_id = update.effective_user.id
    message = update.message.text

    if user_id not in user_data:
        user_data[user_id] = {"state": "start"}

    state = user_data[user_id]["state"]

    # Логика обработки сообщений
    if "/start" in message:
        await update.message.reply_text("Чем могу помочь?")
    elif "привет" in message.lower():
        await update.message.reply_text("Рад снова Вас видеть!")
    else:
        await update.message.reply_text("Обрабатываю...")
        try:
            resp = await uscase.solve(message)
            if resp.status in (Status.CALCULATED.value, Status.CALCULATED_MORE_ROOTS.value):
                answer = "Ответ:\n"
                if resp.status == Status.CALCULATED_MORE_ROOTS.value:
                    answer = "Найдено больше корней:\n"

                roots = resp.roots
                if len(resp.aproxRoots) > 0:
                    roots = resp.aproxRoots
                    
                for root in roots:
                    answer += root + "\n"
                await update.message.reply_text(answer)

            elif resp.status == Status.NEGATIVE_DISCRIMINANT.value:
                await update.message.reply_text("Отрицательный дскриминант. Нет действительных корней.")
                answer = "Ответ с комплексными числами:\n"
                for root in resp.roots:
                    answer += root + "\n"
                await update.message.reply_text(answer)

            elif resp.status in (Status.ERROR.value, Status.NONE.value):
                await update.message.reply_text("Не понял Вас. Возможно, в уравнении есть ошибка. Попробуйте переформулировать свой вопрос.")
                await update.message.reply_text("Напишите мне линейное, квадратное или рациональное уравнение. Переменные должны быть записаны латинскими буквами.")

            elif resp.status in (Status.ERROR_CLIENT.value, Status.ERROR_CLIENT.value):
                await update.message.reply_text("Ошибка на сервере. Попробуйте позже.")

        except Exception as e:
            print(e)
            await update.message.reply_text("Произошла ошибка на сервере")

# Основная функция для запуска бота
def main():
    token = config.telegram.token

    # Создаем приложение
    application = Application.builder().token(token).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()


'''

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from handlers.msg_handler import MsgHandler
from config.config import config
from clients.qwen.qwen_client import QwenClient as q

handler = MsgHandler()
user_data = {}

class Server:
    # Обработчик команды /start
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text("Привет! Я твой бот. Отправь мне любое сообщение, и я отвечу.")

    # Обработчик текстовых сообщений
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
                await update.message.reply_text("Напиши мне линейное, квадратное или рациональное уравнение.")
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
    async def error(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        print(f'Ошибка: {context.error}')

    # Основная функция для запуска бота
    async def run(self):
        # Создаем приложение
        application = Application.builder().token(config.telegram.token).build()

        # Регистрируем обработчики
        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

        # Запускаем бота
        await application.run_polling()

if __name__ == "__main__":
    import asyncio
    server = Server()
    asyncio.run(server.run())
'''