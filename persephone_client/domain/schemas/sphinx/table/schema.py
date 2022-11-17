from pydantic import BaseModel, constr, UUID4


class TableSchema(BaseModel):  # TODO: Ver se ainda é usado, se não for: deletar
    device_id: str
    device_info: dict
    stone_age_id: constr(min_length=2)
    unique_id: UUID4
    status: constr(min_length=2)
    cpf: constr(min_length=2)




