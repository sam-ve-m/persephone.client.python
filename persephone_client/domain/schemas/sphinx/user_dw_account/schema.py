from pydantic import BaseModel


class UserDwAccount(BaseModel):
    unique_id: str
    account: str
    display_account: str
