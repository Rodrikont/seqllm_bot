from config.config import config
from handlers.msg_handler import MsgHandler
from server.bot_server import Server
import asyncio

# v0.1

print()
print("Bot version:\t" + config.app_version)
print()
print("Hello from MYSHLER community")
print()

server = Server()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    if loop.is_running():
        # Если цикл событий уже запущен, используем create_task
        asyncio.create_task(server.run())
    else:
        # Если цикл событий не работает, то запускаем его
        loop.run_until_complete(server.run())
