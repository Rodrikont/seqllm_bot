from pydantic import BaseModel
from typing import Optional

class EqServerBotRespDTO(BaseModel):
    message: list
    status: Optional[int] = 200