from pydantic import BaseModel
from typing import Optional

class EqServerBotRespDTO(BaseModel):
    message: str
    status: Optional[int] = 200