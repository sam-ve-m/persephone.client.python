from pydantic import BaseModel


class UserDocumentSchema(BaseModel):
    unique_id: str
    path_document_front: str
    path_document_back: str
