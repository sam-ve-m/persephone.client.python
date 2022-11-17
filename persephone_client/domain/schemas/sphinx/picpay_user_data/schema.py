from pydantic import BaseModel


class PicpayUserData(BaseModel):
    unique_id: str
    device_id: str
    device_info: dict
    fields: dict
