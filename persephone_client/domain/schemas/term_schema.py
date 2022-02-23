from pydantic import BaseModel, constr


class TermsMetadataSchema(BaseModel):
    user_email: constr(min_length=2)


class TermsSchema(BaseModel):
    metadata: TermsMetadataSchema
    term_type: constr(min_length=2)
    term_version: constr(min_length=2)
    user_accept: bool
    term_answer_time_stamp: int
