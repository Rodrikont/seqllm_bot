from config.config import config
from clients.eqloverllm_client import EqSolverClient
from models.uscase_solver_response import UscaseSolverResponse
from enums.status_enums import Status

class SolverUsecase:
    async def solve(self, message):
        resp = EqSolverClient.solve(message)

        if resp is not None:
            print("Return message from client:\tSucsess")

            response = UscaseSolverResponse(
                status=resp.status,
                roots=resp.roots,
                aproxRoots=resp.aproxRoots,
            )
        else:
            print("Return message from client:\t!!! Error !!!")
            response = UscaseSolverResponse(
                status=Status.ERROR.value,
            )
        
        print(response)
        return response
