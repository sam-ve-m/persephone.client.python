from pydantic import BaseModel


class ScoreValidationStatus(BaseModel):
    unique_id: str
    status: str
