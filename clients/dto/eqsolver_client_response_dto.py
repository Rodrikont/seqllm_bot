from pydantic import BaseModel
from typing import Optional
from clients.dto.eqsolver_client_data import EqClientData

class EqClientResponseDto(BaseModel):
    status: int
    data: EqClientData