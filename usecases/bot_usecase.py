from config.config import config
from models.usecase_bot_request import UsecaseBotReq
from models.uscase_bot_response import UscaseBotResp
from models.client_bot_request import ClientBotReq

class BotUsecase:
    def __init__(self):
        self.config = config

    def execute(self, message: str) -> UsecaseBotReq:
        resp = BotUsecase.req_to_server(message)

        if resp is not None:
            print("Return message from client:\tSucsess")

            response = UscaseBotResp(
                answer=resp.answer,
                status=200,
                error=resp.error
                )
        else:
            print("Return message from client:\t!!! Error !!!")
            response = UscaseBotResp(
                answer="error",
                status=400,
                error="No answer from client"
                )
        
        return response

    def req_to_server(self, message: str) -> ClientBotReq:
        pass