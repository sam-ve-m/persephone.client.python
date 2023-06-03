from pydantic import BaseModel


class CpfValidation(BaseModel):
    cpf: str
    birth_date: float
    name: str
