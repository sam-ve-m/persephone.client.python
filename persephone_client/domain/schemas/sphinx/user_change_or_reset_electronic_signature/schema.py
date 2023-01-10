from pydantic import BaseModel, UUID4, constr


class UserChangeOrResetElectronicSignatureSchema(BaseModel):
    unique_id: UUID4
    device_id: str
    device_info: dict
    previous_electronic_signature: constr(min_length=2)
    previous_is_blocked_electronic_signature: bool
    previous_electronic_signature_wrong_attempts: int
    new_electronic_signature: constr(min_length=2)
    new_is_blocked_electronic_signature: bool
    new_electronic_signature_wrong_attempts: int
