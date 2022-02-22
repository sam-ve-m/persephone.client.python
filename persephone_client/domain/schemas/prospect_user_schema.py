from pydantic import BaseModel


class ProspectUserSchema(BaseModel):
    user_email: str
    nick_name: str
    create_user_time_stamp: int
