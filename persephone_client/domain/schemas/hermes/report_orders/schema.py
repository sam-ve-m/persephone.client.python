from pydantic import BaseModel


class ReportOrders(BaseModel):
    ip: str
    cl_order_id: str
    jwt: str
    request_hash: str
    fix_response: dict
    connection_unique_id: int
