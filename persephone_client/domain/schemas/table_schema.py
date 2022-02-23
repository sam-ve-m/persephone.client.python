from pydantic import BaseModel, constr, UUID4


class TableSchema(BaseModel):
    stone_age_id: constr(min_length=2)
    unique_id: UUID4
    status: constr(min_length=2)
    cpf: int



