from pydantic import BaseModel


class UserExchangeAccountStatus(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    status: str
