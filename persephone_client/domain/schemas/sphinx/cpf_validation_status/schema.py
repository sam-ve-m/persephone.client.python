from pydantic import BaseModel


class CpfValidationStatus(BaseModel):
    cpf: str
    status: str
