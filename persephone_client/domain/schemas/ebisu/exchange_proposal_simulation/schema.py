from pydantic import BaseModel


class ExchangeProposalSimulation(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    proposal_data: dict
