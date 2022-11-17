from pydantic import BaseModel


class HermesSessionAuthenticity(BaseModel):
    ip: str
    device_id: str
    device_info: dict
    jwt: str
    is_authentic: bool
    connection_unique_id: int
