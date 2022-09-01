from pydantic import BaseModel


class UserW8FormConfirmationUsSchema(BaseModel):
    unique_id: str
    w8_form_confirmation: bool

