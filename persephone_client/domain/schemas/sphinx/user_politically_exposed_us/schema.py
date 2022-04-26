from typing import List

from pydantic import BaseModel


class UserPoliticallyExposedUsSchema(BaseModel):
    unique_id: str
    politically_exposed: bool
    politically_exposed_names: List[str]
