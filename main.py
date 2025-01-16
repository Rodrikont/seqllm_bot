from config.config import config
from handlers.msg_handler import MsgHandler
# from server.bot_server import Server
from server import bot_server
import asyncio

# v0.1

print()
print("Bot version:\t" + config.app_version)
print()
print("Hello from MYSHLER community")
print()

server = bot_server

# Основной блок запуска
if __name__ == "__main__":
    asyncio.run(server.main())

