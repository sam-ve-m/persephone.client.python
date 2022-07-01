from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime
from persephone_client.domain.schemas.common.device_info import DeviceInformationOptional


class BankAccounts(BaseModel):
    bank: Optional[str]
    account_type: Optional[str]
    agency: Optional[str]
    account_number: Optional[str]
    account_name: str
    id: UUID4


class UpdateUserBankAccounts(BaseModel):
    bank_account: BankAccounts
    unique_id: UUID4
    device_info: DeviceInformationOptional
    _created_at: datetime
