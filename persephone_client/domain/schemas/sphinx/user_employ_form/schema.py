from pydantic import BaseModel


class UserEmployFormSchema(BaseModel):
    unique_id: str
    employ_status: str
    employ_type: str
    employ_position: str
    employ_company_name: str
