from pydantic import BaseModel, constr, UUID4
from typing import List


class FormList(BaseModel):
    question_id: int
    answer: constr(min_length=2)


class SuitabilitySchema(BaseModel):
    unique_id: UUID4
    form: List[FormList]
    version: int
    score: float
    profile: constr(min_length=2)
    create_suitability_time_stamp: int
