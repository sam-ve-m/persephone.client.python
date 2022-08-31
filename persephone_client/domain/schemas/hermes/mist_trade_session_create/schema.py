from pydantic import BaseModel


class MistTradeSessionCreate(BaseModel):
    ip: str
    jwt: str
    created: bool
    jwt_token_session: str
    message: str
    signature_expire_time: int
    unique_id: str
    connection_unique_id: int
