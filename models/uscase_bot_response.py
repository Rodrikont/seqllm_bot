from pydantic import BaseModel
from typing import Optional
from client_bot_response import ClientBotResp

class UscaseBotResp(BaseModel):
    answer: str
    status: int
    error: Optional[str] = None
    data: ClientBotResp