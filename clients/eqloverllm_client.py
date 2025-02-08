from clients.dto.eqsolver_client_response_dto import EqClientResponseDto
from clients.dto.eqsolver_client_request_dto import EqClientRequestDto
from models.client_solver_response import ClientSolverResponse
from config.config import config
from enums.status_enums import Status
import requests

class EqSolverClient:
    def solve(message: str) -> ClientSolverResponse:
        try:
            print(message)

            print("Send message to server")

            response = None

            req = EqClientRequestDto(
                question=message
            )

            req_json = req.dict()
            path = "{}/{}".format(config.client_solver.url(), config.client_solver.endp_eq)

            resp = requests.post(
                url=path, 
                json=req_json,
            )

            if resp.status_code == 200:
                print(resp)
                try:
                    resp.raise_for_status()
                    respo = resp.json()
                    print(respo)
                    respDto = EqClientResponseDto.parse_obj(respo)
                except ValueError as e:                    
                    print(f"Ошибка разбора JSON: {e}")
                except Exception as e:
                    print(e)
                    return ClientSolverResponse(
                        status=Status.ERROR.value,
                        error=f"Ошибка преобразования ответа: {e}",
                        )
            else:
                print(f"Ошибка запроса: {resp.status_code}")
                return ClientSolverResponse(
                        status=Status.ERROR_CLIENT.value,
                        error=f"Ошибка запроса: {resp.status_code}",
                        )

            if respDto != None:
                    response = ClientSolverResponse(
                        status=respDto.data.status,
                        roots=respDto.data.roots,
                        aproxRoots=respDto.data.aproxRoots,
                        answer=respDto.data.answer,
                        error=respDto.data.error,
                    )
            else:
                print("Empty answer")
                response = ClientSolverResponse(
                    status=Status.ERROR.value,
                    error="Empty answer",
                )

        except requests.exceptions.RequestException as e:
            print(f"Can't connect to server\n\n{e}\n")

            response = ClientSolverResponse(
                status=Status.ERROR_CLIENT_CONNECT.value,
                error="Server now isn't avaliable",
            )

        except ValueError as e:
            print("Can't read answer")
            response = ClientSolverResponse(
                status=Status.ERROR.value,
                error="Can't read answer",
            )

        print(response)
        return response