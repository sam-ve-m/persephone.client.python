from pydantic import BaseModel


class ScoreValidation(BaseModel):
    unique_id: str
    name: str
    birth_date: int
    gender: str
    mother_name: str
    nationality: int
