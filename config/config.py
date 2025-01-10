from environs import Env

class Config:
    def __init__(self):
        env = Env()
        env.read_env()  # Загружает переменные из .env файла

        self.app_name = env.str("APP_NAME", "SEBot")
        self.app_version = env.str("APP_VERSION", "0.1")
        self.debug = env.bool("APP_DEBUG", False)
        self.tg_token = env.str("TELEGRAM_TOKEN", "7941346515:AAHFOqVTjrlIVGuR1BMEG9WEXXtj4YEGyWA")
        self.server_host = env.str("SERVER_HOST", "0.0.0.0")
config = Config()