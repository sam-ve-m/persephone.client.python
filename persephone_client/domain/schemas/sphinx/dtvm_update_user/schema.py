from pydantic import BaseModel, constr
from typing import Optional


class DtvmUpdateStringField(BaseModel):
    previous_data: constr(min_length=2)
    new_data: constr(min_length=2)


class DtvmUpdateIntegerField(BaseModel):
    previous_data: int
    new_data: int


class DtvmUpdateFloatField(BaseModel):
    previous_data: float
    new_data: float


class DtvmUpdateBooleanField(BaseModel):
    previous_data: bool
    new_data: bool


class PoliticallyExposedPersonSchema(BaseModel):
    is_politically_exposed_person: DtvmUpdateBooleanField


class DocumentsPhotosSchema(BaseModel):
    identifier_document: DtvmUpdateStringField
    address_document: DtvmUpdateStringField


class EducationSchema(BaseModel):
    level: DtvmUpdateStringField
    course: Optional[DtvmUpdateStringField]


class AssetsSchema(BaseModel):
    patrimony: DtvmUpdateFloatField
    income: DtvmUpdateFloatField


class CompanySchema(BaseModel):
    name: DtvmUpdateStringField
    cnpj: DtvmUpdateIntegerField


class OccupationSchema(BaseModel):
    status: DtvmUpdateStringField
    company: Optional[CompanySchema]


class DocumentDataSchema(BaseModel):
    number: DtvmUpdateStringField
    date: DtvmUpdateIntegerField
    state: DtvmUpdateStringField
    issuer: DtvmUpdateStringField


class IdentifierDocumentSchema(BaseModel):
    type: DtvmUpdateStringField
    document_data: DocumentDataSchema


class Suitability(BaseModel):
    score: DtvmUpdateFloatField
    profile: DtvmUpdateStringField
    version: DtvmUpdateIntegerField
    done_time_stamp: DtvmUpdateIntegerField


class Spouse(BaseModel):
    spouse_name: DtvmUpdateStringField
    nationality: DtvmUpdateStringField
    cpf: DtvmUpdateIntegerField


class MaritalSchema(BaseModel):
    status: DtvmUpdateStringField
    spouse: Spouse


class AddressSchema(BaseModel):
    street_name: DtvmUpdateStringField
    number: DtvmUpdateIntegerField
    state: DtvmUpdateStringField
    city: DtvmUpdateStringField
    zipCode: DtvmUpdateStringField
    phone_number: DtvmUpdateStringField


class DtvmUpdateUserUpdatedData(BaseModel):
    name: DtvmUpdateStringField
    address: AddressSchema
    marital: MaritalSchema
    suitability: Suitability
    is_cvm_qualified_investor: DtvmUpdateBooleanField
    gender: DtvmUpdateStringField
    identifier_document: IdentifierDocumentSchema
    occupation: OccupationSchema
    assets: AssetsSchema
    education: EducationSchema
    documents_photos: DocumentsPhotosSchema
    politically_exposed_person: PoliticallyExposedPersonSchema


class DtvmUpdateUserMetadataSchema(BaseModel):
    user_email: constr(min_length=2)
    digital_signature_time_stamp: int


class DtvmUpdateUserSchema(BaseModel):
    device_id: str
    device_info: dict
    metadata: DtvmUpdateUserMetadataSchema
    updated_user_data: DtvmUpdateUserUpdatedData
    validate_user_time_stamp: int
