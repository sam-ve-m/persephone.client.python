from pydantic import BaseModel
from typing import Optional


class IntegerProvidedByBureaux(BaseModel):
    value: int
    source: str


class StringProvidedByBureaux(BaseModel):
    value: str
    source: str


class NumberProvidedByBureaux(BaseModel):
    value: float
    source: str


class BooleanProvidedByBureaux(BaseModel):
    value: bool
    source: str


class PoliticallyExposedPersonSchema(BaseModel):
    is_politically_exposed_person: BooleanProvidedByBureaux


class DocumentsPhotosSchema(BaseModel):
    identifier_document: StringProvidedByBureaux
    address_document: StringProvidedByBureaux


class StringEducationCurse(BaseModel):
    value: Optional[str]
    source: Optional[str]


class EducationSchema(BaseModel):
    level: StringProvidedByBureaux
    course: Optional[StringEducationCurse]


class AssetsSchema(BaseModel):
    patrimony: NumberProvidedByBureaux
    income: NumberProvidedByBureaux


class CompanySchema(BaseModel):
    name: StringProvidedByBureaux
    cnpj: IntegerProvidedByBureaux


class OccupationSchema(BaseModel):
    status: StringProvidedByBureaux
    company: Optional[CompanySchema]


class AddressSchema(BaseModel):
    street_name: StringProvidedByBureaux
    number: IntegerProvidedByBureaux
    state: StringProvidedByBureaux
    city: StringProvidedByBureaux
    zipCode: StringProvidedByBureaux
    phone_number: StringProvidedByBureaux


class DocumentDataSchema(BaseModel):
    number: StringProvidedByBureaux
    date: IntegerProvidedByBureaux
    state: StringProvidedByBureaux
    issuer: StringProvidedByBureaux


class IdentifierDocumentSchema(BaseModel):
    type: StringProvidedByBureaux
    document_data: DocumentDataSchema


class ProvidedByBureauxSchema(BaseModel):
    gender: StringProvidedByBureaux
    birthDate: IntegerProvidedByBureaux
    naturalness: StringProvidedByBureaux
    nationality: StringProvidedByBureaux
    mother_name: StringProvidedByBureaux
    identifier_document: IdentifierDocumentSchema
    address: AddressSchema
    occupation: OccupationSchema
    assets: AssetsSchema
    education: EducationSchema
    documents_photos: DocumentsPhotosSchema
    politically_exposed_person: PoliticallyExposedPersonSchema
    date_of_acquisition: IntegerProvidedByBureaux


class UsPerson(BaseModel):
    is_us_person: bool
    us_tin: str


class ThirdPartyOperator(BaseModel):
    is_third_party_operator: bool
    details: dict
    third_party_operator_email: str


class Spouse(BaseModel):
    spouse_name: str
    nationality: str
    cpf: int


class MaritalSchema(BaseModel):
    status: str
    spouse: Spouse


class ProvidedByUserSchema(BaseModel):
    name: str
    marital: MaritalSchema
    cpf: int
    email: str
    can_be_managed_by_third_party_operator: bool
    is_managed_by_third_party_operator: bool
    third_party_operator: ThirdPartyOperator
    is_cvm_qualified_investor: bool
    us_person: UsPerson


class UserRegistrySchema(BaseModel):
    provided_by_user: ProvidedByUserSchema
    provided_by_bureaux: ProvidedByBureauxSchema


class UserMetadataSchema(BaseModel):
    user_email: str


class DtvmUserSchema(BaseModel):
    metadata: UserMetadataSchema
    user_registry_data: UserRegistrySchema
    create_user_time_stamp: int
    create_digital_signature_time_stamp: int

