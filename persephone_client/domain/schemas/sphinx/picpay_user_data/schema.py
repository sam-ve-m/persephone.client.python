from pydantic import BaseModel


class PicpayUserData(BaseModel):
    unique_id: str
    fields: dict
