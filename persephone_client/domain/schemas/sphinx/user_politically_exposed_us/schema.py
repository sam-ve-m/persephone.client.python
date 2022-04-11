from pydantic import BaseModel


class UserPoliticallyExposedUsSchema(BaseModel):
    unique_id: str
    politically_exposed: bool
