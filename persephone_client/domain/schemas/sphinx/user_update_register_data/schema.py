from typing import Optional

from pydantic import BaseModel, UUID4


class UserUpdateRegisterDataSchema(BaseModel):
    unique_id: UUID4
    device_id: Optional[str]
    device_info: Optional[dict]
    modified_register_data: dict
    update_customer_registration_data: dict
