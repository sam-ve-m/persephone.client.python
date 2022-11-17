from pydantic import BaseModel, constr, UUID4, conlist


class FormList(BaseModel):
    question_order_id: int
    answer_option_id: int


class SuitabilitySchema(BaseModel):
    unique_id: UUID4
    device_id: str
    device_info: dict
    form: conlist(item_type=FormList, min_items=1)
    version: int
    score: float
    profile: int
