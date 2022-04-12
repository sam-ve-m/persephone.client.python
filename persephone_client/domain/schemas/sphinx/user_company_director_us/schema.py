from pydantic import BaseModel


class UserCompanyDirectorUsSchema(BaseModel):
    unique_id: str
    company_director: bool
    company_director_from: str
