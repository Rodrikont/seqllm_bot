from environs import Env

class Config:
    def __init__(self):
        env = Env()
        env.read_env()  # Загружает переменные из .env файла

        self.app_name = env.str("APP_NAME", "SEqBot")
        self.app_version = env.str("APP_VERSION", "v0.1.1")
        self.debug = env.bool("APP_DEBUG", False)
        self.tg_token = env.str("EQ_TELEGRAM_TOKEN", "")
        self.client_url = env.str("CLIENT_EQ_URL", "http://0.0.0.0:8080")
        self.equation_endp = env.str("CLIENT_EQ_ENDPOINT", "/equation/")
config = Config()