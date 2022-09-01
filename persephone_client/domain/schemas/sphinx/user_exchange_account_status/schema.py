from pydantic import BaseModel


class UserExchangeAccountStatus(BaseModel):
    unique_id: str
    status: str
    cpf: str
    exchange_account: dict
