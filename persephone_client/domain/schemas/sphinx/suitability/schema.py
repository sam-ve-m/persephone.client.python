from pydantic import BaseModel, constr, UUID4, conlist


class FormList(BaseModel):
    question_id: int
    answer: constr(min_length=2)


class SuitabilitySchema(BaseModel):
    unique_id: UUID4
    form: conlist(item_type=FormList, min_items=1)
    version: int
    score: float
    profile: constr(min_length=2)
    create_suitability_time_stamp: int
