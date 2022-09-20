from pydantic import BaseModel


class UserExchangeAccount(BaseModel):
    unique_id: str
    cpf: str
    exchange_account: dict
