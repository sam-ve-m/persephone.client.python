from pydantic import BaseModel, UUID4, constr
from typing import Optional


class SpouseSchema(BaseModel):
    nationality: constr(min_length=1)
    cpf: constr(min_length=2)
    name: constr(min_length=2)


class MaritalSchema(BaseModel):
    status: int
    spouse: Optional[SpouseSchema]


class UserComplementaryDataSchema(BaseModel):
    unique_id: UUID4
    device_id: str
    device_info: dict
    marital: MaritalSchema
