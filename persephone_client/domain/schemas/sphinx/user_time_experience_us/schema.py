from pydantic import BaseModel


class UserTimeExperienceUsSchema(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    time_experience: str
