from pydantic import BaseModel


class HermesSessionIntegrity(BaseModel):
    ip: str
    device_id: str
    device_info: dict
    jwt: str
    is_integrity: bool
    jwt_missing_fields: list
    connection_unique_id: int
