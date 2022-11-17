from pydantic import BaseModel


class ScoreValidationStatus(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    status: str
