from pydantic import BaseModel
from typing import Optional

class EqServerBotResp(BaseModel):
    answer: str
    status: int
    error: Optional[str] = None