from pydantic import BaseModel
from typing import Optional


class UserCompanyDirectorUsSchema(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    company_director: bool
    company_director_of: Optional[str]
