from pydantic import BaseModel
from typing import Optional


class UserTaxResidencesUsSchema(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    tax_residences: Optional[dict]
