from pydantic import BaseModel


class UserExchangeAccountStatus(BaseModel):  # TODO: Criar schema no Persephone Server
    unique_id: str
    status: str
    cpf: str
    exchange_account: dict
