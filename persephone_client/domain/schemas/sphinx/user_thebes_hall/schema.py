from pydantic import BaseModel, UUID4, constr


class UserThebesHallSchema(BaseModel):
    unique_id: UUID4
    device_id: str
    device_info: dict
    jwt: constr(min_length=2)
    jwt_payload_data: dict
