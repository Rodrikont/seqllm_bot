from config.config import config
# from server.bot_server import Server
from server import bot_server
import asyncio

print()
print("Bot version:\t" + config.app_version)
print()

server = bot_server

# Основной блок запуска
if __name__ == "__main__":
    print("Starting the application...")
    asyncio.run(server.main())

