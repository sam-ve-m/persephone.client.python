from typing import List

from pydantic import BaseModel


class SignedTermSchema(BaseModel):
    unique_id: str
    terms_type: List[str]
    terms_update: dict
    user_accept: bool
    term_answer_time_stamp: int
