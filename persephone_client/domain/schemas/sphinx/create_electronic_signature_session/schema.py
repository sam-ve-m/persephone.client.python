from pydantic import BaseModel, UUID4, constr


class MistSessionSchema(BaseModel):
    created: bool
    jwt_token_session: constr(min_length=2)
    message: constr(min_length=2)


class CreateElectronicSignatureSessionSchema(BaseModel):
    unique_id: UUID4
    mist_session: MistSessionSchema
    allowed: bool
