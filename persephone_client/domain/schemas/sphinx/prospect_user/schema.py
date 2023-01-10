from pydantic import BaseModel, UUID4, constr


class ProspectUserSchema(BaseModel):
    unique_id: UUID4
    device_id: str
    device_info: dict
    nick_name: constr(min_length=2)
