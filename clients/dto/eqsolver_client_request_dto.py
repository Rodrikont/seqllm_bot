from pydantic import BaseModel

class EqClientRequestDto(BaseModel):
    question: str
    