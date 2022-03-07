from pydantic import BaseModel, UUID4, constr


class UserThebesHallSchema(BaseModel):
    unique_id: UUID4
    jwt: constr(min_length=2)
    jwt_payload_data: dict
    device_information: dict
