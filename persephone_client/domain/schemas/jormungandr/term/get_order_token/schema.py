from pydantic import BaseModel

from persephone_client.domain.enums.quote_type.enum import QuoteType
from persephone_client.domain.enums.risk_classification.enum import RiskClassification


class GetOrderTokenVariableIncome(BaseModel):
    unique_id: str
    token: str
    symbol: str
    quantity: int
    quote_type: QuoteType


class GetOrderTokenFixedIncome(BaseModel):
    unique_id: str
    token: str
    product_id: int
    cash_amount: float
    risk: RiskClassification
