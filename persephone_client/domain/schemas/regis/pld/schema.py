from typing import Optional
from pydantic import BaseModel


class Pld(BaseModel):
    unique_id: str
    device_id: Optional[str]
    device_info: Optional[dict]
    score: int
    rating: str
    approval: bool
    validations: dict
    user_data: Optional[dict]
