from typing import Optional
from pydantic import BaseModel


class Pld(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    score: int
    rating: str
    approval: bool
    validations: dict
    user_data: Optional[dict]
