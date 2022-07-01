from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime

from persephone_client.domain.schemas.common.device_info import DeviceInformationOptional


class BankAccounts(BaseModel):
    cpf: str
    bank: str
    account_type: str
    agency: str
    account_number: str
    account_name: Optional[str]
    status: str
    id: UUID4


class RegisterClientBankAccount(BaseModel):
    bank_account: BankAccounts
    unique_id: UUID4
    device_info: DeviceInformationOptional
    _created_at: datetime