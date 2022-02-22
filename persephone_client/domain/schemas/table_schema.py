from pydantic import BaseModel


class TableSchema(BaseModel):
    stone_age_id: str
    user_id: str
    status: str
    cpf: int



