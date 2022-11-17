from pydantic import BaseModel


class ScoreValidation(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    name: str
    birth_date: int
    gender: str
    mother_name: str
    nationality: int
    is_politically_exposed_person: bool
    is_correlated_to_politically_exposed_person: bool
