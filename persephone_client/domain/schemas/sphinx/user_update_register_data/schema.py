from pydantic import BaseModel, UUID4


class UserUpdateRegisterDataSchema(BaseModel):
    unique_id: UUID4
    device_id: str
    device_info: dict
    modified_register_data: dict
    update_customer_registration_data: dict
