from pydantic import BaseModel


class CpfValidationStatus(BaseModel):
    unique_id: str
    status: str
