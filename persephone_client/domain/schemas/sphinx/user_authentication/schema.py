from pydantic import BaseModel, UUID4, constr


class ScopeSchema(BaseModel):
    view_type: constr(min_length=2)
    features: list


class UserAuthenticationSchema(BaseModel):
    unique_id: UUID4
    is_active_user: bool
    scope: ScopeSchema
