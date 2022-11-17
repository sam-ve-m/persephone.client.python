from pydantic import BaseModel


class CashFlowWithdrawalToExternalBank(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    origin_account: dict
    account_destination: dict
    value: float
