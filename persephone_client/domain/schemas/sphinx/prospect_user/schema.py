from pydantic import BaseModel, UUID4, constr


class ProspectUserSchema(BaseModel):
    unique_id: UUID4
    nick_name: constr(min_length=2)
