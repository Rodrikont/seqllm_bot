from config import config
from usecases.bot_usecase import BotUsecase
from models.handler_bot_request import HandlerBotReq
from models.uscase_bot_response import UscaseBotResp

usecase = BotUsecase()

class MsgHandler:        
    def exequte(self, message: str) -> HandlerBotReq:
        print("Send message to usecase")
        resp = usecase.execute(message)
        if resp is not None:
            print("Return message from usecase:\tSucsess")

            response = UscaseBotResp(
                answer=resp.answer,
                status=200,
                error=resp.error
            )
        else:
            print("Return message from usecase:\t!!! Error !!!")

            response = UscaseBotResp(
                answer="error",
                status=500,
                error="No answer from usecase"
            )

        print(response)
        return response

