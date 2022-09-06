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
    unique_id: UUID4
    bank_account: BankAccounts
    device_info: DeviceInformationOptional
