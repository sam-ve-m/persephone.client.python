from pydantic import BaseModel


class CpfValidation(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    birth_date: float
    name: str
