from config.config import config
from clients.eqloverllm_client import EqSolverClient
from models.usecase_bot_request import UsecaseBotReq
from models.uscase_bot_response import UscaseBotResp
from models.client_bot_request import ClientBotReq

client = EqSolverClient()

class BotUsecase:
    def __init__(self):
        self.config = config

    def execute(self, message: str) -> UsecaseBotReq:
        resp = self.msg_to_client(message)

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
                status=500,
                error="No answer from client"
                )
        
        return response

    def msg_to_client(self, message: str) -> ClientBotReq:
        print("Send message to client")
        a = client.request(message)
        return a