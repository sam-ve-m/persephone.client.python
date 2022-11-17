from typing import List

from pydantic import BaseModel


class UserPoliticallyExposedUsSchema(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    politically_exposed: bool
    politically_exposed_names: List[str]
