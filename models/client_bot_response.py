from pydantic import BaseModel
from typing import Optional
from eqserver_bot_response import EqServerBotResp

class ClientBotResp(BaseModel):
    answer: str
    status: int
    error: Optional[str] = None
    data: EqServerBotResp