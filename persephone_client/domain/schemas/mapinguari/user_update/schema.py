from pydantic import BaseModel


class MapinguariUserUpdate(BaseModel):

    access_ip: str
    name_employee: str
    email_employee: str
    to_update_client_obj: dict
    pre_update_client_obj: dict
    update_at: int  # in seconds
