from pydantic import BaseModel


class CpfValidationStatus(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    status: str
