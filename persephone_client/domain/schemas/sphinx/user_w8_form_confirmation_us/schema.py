from pydantic import BaseModel


class UserW8FormConfirmationUsSchema(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    w8_form_confirmation: bool

