from pydantic import BaseModel
from typing import Optional


class UserEmployFormSchema(BaseModel):
    unique_id: str
    employ_status: str
    employ_type: Optional[str]
    employ_position: Optional[str]
    employ_company_name: Optional[str]
