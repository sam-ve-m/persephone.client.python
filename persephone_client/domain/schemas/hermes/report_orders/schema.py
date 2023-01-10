from pydantic import BaseModel


class ReportOrders(BaseModel):
    ip: str
    device_id: str
    device_info: dict
    cl_order_id: str
    jwt: str
    request_hash: str
    fix_response: dict
    connection_unique_id: int
