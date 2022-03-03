from pydantic import BaseModel, constr, UUID4


class UserLogoutSchema(BaseModel):
    unique_id: UUID4
    jwt: constr(min_length=2)
    device_information: dict
