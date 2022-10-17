from pydantic import BaseModel


class Pld(BaseModel):
    unique_id: str
    score: int
    rating: str
    approval: bool
    validations: dict
