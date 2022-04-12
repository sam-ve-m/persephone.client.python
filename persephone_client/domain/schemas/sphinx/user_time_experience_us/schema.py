from pydantic import BaseModel


class UserTimeExperienceUsSchema(BaseModel):
    unique_id: str
    time_experience: str
