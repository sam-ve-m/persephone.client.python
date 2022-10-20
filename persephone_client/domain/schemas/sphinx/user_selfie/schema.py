from pydantic import BaseModel, UUID4, constr


class UserSelfieSchema(BaseModel):
    unique_id: UUID4
    device_id: str
    geolocation: str
    ip_address: str
    device_info: dict
    file_path: constr(min_length=2)
