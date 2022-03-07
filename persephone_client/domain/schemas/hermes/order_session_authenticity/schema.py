from pydantic import BaseModel


class HermesSessionAuthenticity(BaseModel):
    ip: str
    jwt: str
    is_authentic: bool
    connection_unique_id: int
