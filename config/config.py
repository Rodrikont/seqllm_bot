from environs import Env
import os

class Telegram:
    def __init__(self, env: Env):
        self.token = env.str("EQ_TELEGRAM_TOKEN", "")
        self.token_file = env.str("TG_TOKEN_FILE", "/run/secrets/seqllm_telegram_token")

    def init_token(self):
        if self.token == "":
            # Проверка на существование файла
            if os.path.exists(self.token_file):
                # Открытие файла и чтение содержимого
                with open(self.token_file, "r", encoding="utf-8") as file:
                    self.token = file.read()
            else:
                print(f"Файл {self.token_file} не существует.")
class ClientSolver:
    def __init__(self, env: Env):
        self.addr = env.str("CLIENT_EQ_ADDR", "http://0.0.0.0")
        self.port = env.str("CLIENT_EQ_PORT", "8080")
        self.endp_eq = env.str("CLIENT_EQ_ENDP", "equation")

    def url(self):
        return self.addr + ":" + self.port

class Config:
    def __init__(self):
        env = Env()
        # Загружает переменные из .env файла
        env.read_env()

        self.telegram = Telegram(env)
        self.client_solver = ClientSolver(env)

        self.app_name = env.str("APP_NAME", "SEqBot")
        self.app_version = env.str("APP_VERSION", "v0.1.1")
        self.debug = env.bool("APP_DEBUG", False)
        
config = Config()
