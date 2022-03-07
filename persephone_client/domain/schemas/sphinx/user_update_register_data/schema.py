from pydantic import BaseModel, UUID4


class UserUpdateRegisterDataSchema(BaseModel):
    unique_id: UUID4
    modified_register_data: dict
    update_customer_registration_data: dict
