from pydantic import BaseModel


class SentOrders(BaseModel):
    sent_order: dict
    cl_order_id: str
    connection_unique_id: int
