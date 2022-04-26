from pydantic import BaseModel


class UserTaxResidencesUsSchema(BaseModel):
    unique_id: str
    tax_residences: str
