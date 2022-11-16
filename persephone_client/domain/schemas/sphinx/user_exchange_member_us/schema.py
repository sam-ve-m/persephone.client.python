from pydantic import BaseModel


class UserExchangeMemberUsSchema(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    exchange_member: bool
