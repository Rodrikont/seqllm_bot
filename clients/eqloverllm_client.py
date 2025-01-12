from models.eqserver_bot_request import EqServerBotReq
from clients.dto.eqsolver_client_dto import EqServerBotRespDTO
from models.client_bot_request2 import ClientBotReq
from models.client_bot_response import ClientBotResp
from config.config import config
import requests

class EqSolverClient:
    def request(message: str) -> ClientBotReq:
        try:
            print(message)

            json = EqServerBotReq(
                question=message,
                status=200
            )
            
            print(json)

            data = json.dict()

            print(data)

            print("Send message to server")

            resp = requests.post(config.client_solver.url() + "/" + config.client_solver.endp_eq, json=data)

            if resp.status_code == 200:
                try:
                    resp.raise_for_status()
                    respo = resp.json()
                    respDto = EqServerBotRespDTO.parse_obj(respo)
                except ValueError as e:                    
                    print(f"Ошибка разбора JSON: {e}")
                except Exception as e:
                    print(e)
                    return ClientBotResp(error=f"Ошибка преобразования ответа: {e}")
            else:
                print(f"Ошибка запроса: {resp.status_code}")
                return ClientBotResp(error=f"Ошибка запроса: {resp.status_code}")

            if respDto != None:
                answ = respDto.message
                response = ClientBotResp(
                    answer=answ,
                    status=200
                )
            else:
                print("Empty answer")
                response = ClientBotResp(
                    answer="error",
                    status=500,
                    error="Empty answer"
                )

        except requests.exceptions.RequestException as e:
            print(f"Can't connect to server\n\n{e}\n")

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

        print(response)
        return response