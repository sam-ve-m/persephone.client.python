from pydantic import BaseModel


class TermsMetadataSchema(BaseModel):
    user_email: str


class TermsSchema(BaseModel):
    metadata: TermsMetadataSchema
    term_type: str
    term_version: str
    user_accept: bool
    term_answer_time_stamp: int
