from pydantic import BaseModel
from typing import Optional


class UserTaxResidencesUsSchema(BaseModel):
    unique_id: str
    tax_residences: Optional[dict]
