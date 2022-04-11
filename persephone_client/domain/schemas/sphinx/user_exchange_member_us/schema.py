from pydantic import BaseModel


class UserExchangeMemberUsSchema(BaseModel):
    unique_id: str
    exchange_member: bool
