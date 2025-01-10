from pydantic import BaseModel
from typing import Optional
from models.client_bot_response import ClientBotResp

class UscaseBotResp(BaseModel):
    answer: str
    status: int
    error: Optional[str] = None
    data: dict = ClientBotResp