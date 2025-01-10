from pydantic import BaseModel

class UsecaseBotReq(BaseModel):
    message: str