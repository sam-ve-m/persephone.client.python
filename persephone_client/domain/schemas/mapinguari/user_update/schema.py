from pydantic import BaseModel


class MapinguariUserUpdate(BaseModel):

    access_ip: str
    employee_name: str
    employee_email: str
    client_post_update_obj: dict
    client_pre_update_obj: dict
    updated_at: int  # in seconds
