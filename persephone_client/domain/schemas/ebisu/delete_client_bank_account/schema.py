from pydantic import BaseModel, UUID4
from datetime import datetime
from persephone_client.domain.schemas.common.device_info import DeviceInformationOptional


class BankAccount(BaseModel):
    id: str


class DeleteClientBankAccount(BaseModel):
    bank_account: BankAccount
    unique_id: UUID4
    device_info: DeviceInformationOptional
