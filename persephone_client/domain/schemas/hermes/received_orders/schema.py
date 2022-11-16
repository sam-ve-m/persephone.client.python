from pydantic import BaseModel


class ReceivedOrders(BaseModel):
    ip: str
    device_id: str
    device_info: dict
    jwt: str
    jwt_token_session: str
    request: dict
    is_session_valid: bool
    message: str
    cl_order_id: str
    connection_unique_id: str
