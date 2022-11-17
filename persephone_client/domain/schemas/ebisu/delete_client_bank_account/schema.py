from pydantic import BaseModel, UUID4
from datetime import datetime
from persephone_client.domain.schemas.common.device_info import DeviceInformationOptional


class BankAccount(BaseModel):
    id: str


class DeleteClientBankAccount(BaseModel):
    unique_id: UUID4
    device_id: str
    device_info: dict
    bank_account: BankAccount
    device_info: DeviceInformationOptional
    _created_at: datetime
