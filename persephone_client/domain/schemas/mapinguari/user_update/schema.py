from pydantic import BaseModel


class MapinguariUserUpdate(BaseModel):

    access_ip: str
    employee_name: str
    employee_email: str
    post_update_client_obj: dict
    pre_update_client_obj: dict
    client_unique_id: str
    updated_at: int  # in seconds
