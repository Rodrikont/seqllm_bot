from pydantic import BaseModel
from typing import Optional

class EqServerBotResp(BaseModel):
    answer: list
    status: int
    error: Optional[str] = None