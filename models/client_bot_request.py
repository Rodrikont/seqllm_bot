from pydantic import BaseModel
from typing import Optional

class ClientBotReq(BaseModel):
    message: str
    status: int
    error: Optional[str] = None