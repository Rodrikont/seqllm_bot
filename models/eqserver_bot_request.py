from pydantic import BaseModel
from typing import Optional

class EqServerBotReq(BaseModel):
    question: str
    status: int