from pydantic import BaseModel, UUID4, constr


class UserSelfieSchema(BaseModel):
    unique_id: UUID4
    file_path: constr(min_length=2)