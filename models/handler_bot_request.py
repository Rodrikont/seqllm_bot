from pydantic import BaseModel
from typing import Optional

class HandlerBotReq(BaseModel):
    message: str
    status: int
    error: Optional[str] = None