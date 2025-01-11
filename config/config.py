from environs import Env

class Config:
    def __init__(self):
        env = Env()
        env.read_env()  # Загружает переменные из .env файла

        self.app_name = env.str("APP_NAME", "SEBot")
        self.app_version = env.str("APP_VERSION", "v0.1.1")
        self.debug = env.bool("APP_DEBUG", False)
        self.tg_token = env.str("TELEGRAM_TOKEN", "7941346515:AAHFOqVTjrlIVGuR1BMEG9WEXXtj4YEGyWA")
        self.client_url = env.str("CLIENT_URL", "http://0.0.0.0:8080/")
        self.equation_endp = env.str("EQ_ENDP", "equation/")
config = Config()