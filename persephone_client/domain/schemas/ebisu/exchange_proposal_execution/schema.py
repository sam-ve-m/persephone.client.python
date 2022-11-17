from datetime import datetime
from pydantic import BaseModel


class ExchangeProposalExecution(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    origin_account_number: str
    origin_country: str
    destination_account_number: str
    destination_country: str
    exchange_proposal_value: str
    halberd_country: str
    operation_type: str
    next_d2: datetime
    token: str
    execution_report: dict

