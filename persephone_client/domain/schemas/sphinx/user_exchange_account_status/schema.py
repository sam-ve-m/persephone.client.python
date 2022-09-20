from pydantic import BaseModel


class UserExchangeAccountStatus(BaseModel):
    unique_id: str
    status: str
