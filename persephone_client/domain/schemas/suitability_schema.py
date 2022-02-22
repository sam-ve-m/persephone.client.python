from pydantic import BaseModel
from typing import List


class FormList(BaseModel):
    question_id: int
    answer: str


class MetadataSuitabilitySchema(BaseModel):
    user_email: str


class SuitabilitySchema(BaseModel):
    metadata: MetadataSuitabilitySchema
    form: List[FormList]
    version: int
    score: float
    profile: str
    create_suitability_time_stamp: int
