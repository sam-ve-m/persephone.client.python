from pydantic import BaseModel


class CpfValidation(BaseModel):
    unique_id: str
    birth_date: float
    name: str
