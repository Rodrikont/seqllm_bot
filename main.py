from config.config import config
from handlers.msg_handler import MsgHandler
from server.bot_server import Server

# v0.1

print()
print("Bot version:\t" + config.app_version)
print()
print("Hello from MYSHLER community")
print()

server = Server()

if __name__ == "__main__":
    server.serve()
