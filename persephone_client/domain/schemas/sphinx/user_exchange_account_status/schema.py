from pydantic import BaseModel
from typing import Optional


class UserExchangeAccountStatus(BaseModel):
    unique_id: str
    status: str
    cpf: str
    exchange_account: dict
