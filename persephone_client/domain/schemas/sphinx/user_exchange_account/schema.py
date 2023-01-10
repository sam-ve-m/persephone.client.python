from pydantic import BaseModel


class UserExchangeAccount(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    cpf: str
    exchange_account: dict
