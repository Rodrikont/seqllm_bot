from models.eqserver_bot_request import EqServerBotReq
from models.client_bot_request2 import ClientBotReq
from models.client_bot_response import ClientBotResp
from config.config import config
import requests

class EqSolverClient:
    def request(message: str) -> ClientBotReq:
        try:
            json = {
                "equation": f"{message}"
            }

            print(message)
            
            print(json)

            print("Send message to server")

            resp = requests.post("http://0.0.0.0:8080/equation", data=json)

            resp.raise_for_status()

            respo = resp.json()

            response = ClientBotResp(
                answer=respo.get('answer'),
                status=200
            )
        except requests.exceptions.RequestException as e:
            print(f"Can't connect to server\n\n{e}")

            response = ClientBotResp(
                answer="error",
                status=404,
                error="Server now isn't avaliable"
            )

        except ValueError as e:
            print("Can't read answer")
            response = ClientBotResp(
                answer="error",
                status=500,
                error="Can't read answer"
            )

        return response