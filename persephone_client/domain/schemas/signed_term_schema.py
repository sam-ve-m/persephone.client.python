from pydantic import BaseModel, UUID4, constr


class SignedTermSchema(BaseModel):
    unique_id: UUID4
    term_type: constr(min_length=2)
    term_version: constr(min_length=2)
    user_accept: bool
    term_answer_time_stamp: int
