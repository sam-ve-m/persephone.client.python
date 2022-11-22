from pydantic import BaseModel, constr, UUID4


class UserLogoutSchema(BaseModel):
    unique_id: UUID4
    device_id: str
    device_info: dict
    jwt: constr(min_length=2)
