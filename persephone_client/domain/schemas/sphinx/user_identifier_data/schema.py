from pydantic import BaseModel, UUID4, constr, conlist


class TaxResidences(BaseModel):
    country: constr(min_length=2)
    tax_number: constr(min_length=2)


class UserIdentifierDataSchema(BaseModel):
    unique_id: UUID4
    device_id: str
    device_info: dict
    cpf: constr(min_length=2)
    cel_phone: constr(min_length=2)
    tax_residences: conlist(item_type=TaxResidences, min_items=0)
