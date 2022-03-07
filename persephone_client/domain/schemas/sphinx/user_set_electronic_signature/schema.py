from pydantic import BaseModel, UUID4, constr


class UserSetElectronicSignatureSchema(BaseModel):
    unique_id: UUID4
    electronic_signature: constr(min_length=2)
    is_blocked_electronic_signature: bool
    electronic_signature_wrong_attempts: int
