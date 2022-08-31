from pydantic import BaseModel, UUID4, constr


class ProspectUserSchema(BaseModel):
    unique_id: UUID4
    email: constr(min_length=2)
    nick_name: constr(min_length=2)
