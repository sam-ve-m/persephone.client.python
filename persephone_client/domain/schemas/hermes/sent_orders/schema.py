from pydantic import BaseModel


class SentOrders(BaseModel):
    sent_order: dict
    device_id: str
    device_info: dict
    cl_order_id: str
    connection_unique_id: int
