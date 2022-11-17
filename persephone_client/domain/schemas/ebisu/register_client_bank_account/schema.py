from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime

from persephone_client.domain.schemas.common.device_info import DeviceInformationOptional


class BankAccounts(BaseModel):
    bank: str
    account_type: str
    agency: str
    account_number: str
    account_name: Optional[str]
    status: str
    id: UUID4


class RegisterClientBankAccount(BaseModel):
    unique_id: UUID4
    device_id: str
    device_info: dict
    bank_account: BankAccounts
    device_info: DeviceInformationOptional
    _created_at: datetime