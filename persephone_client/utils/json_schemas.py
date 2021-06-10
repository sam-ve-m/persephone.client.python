# "DTVM USER SCHEMA"
dtvm_user_schema = {
    "type": "object",
    "properties": {
        "metadata": {"type": "object"},
        "user_registry_data": {"type": "object"},
        "create_user_time_stamp": {"type": "integer"},
        "create_digital_signature_time_stamp": {"type": "integer"}
    },
    "required": [
        "metadata",
        "user_registry_data",
        "create_user_time_stamp",
        "create_digital_signature_time_stamp",
    ],
}

user_metadata_schema = {
    "type": "object",
    "properties": {"user_email": {"type": "string"}},
    "required": ["user_email"],
}

user_registry_schema = {
    "type": "object",
    "properties": {
        "provided_by_user": {"type": "object"},
        "provided_by_bureaux": {"type": "object"},
    },
    "required": ["provided_by_user", "provided_by_bureaux"],
}

provided_by_user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "marital": {"type": "object"},
        "cpf": {"type": "integer"},
        "email": {"type": "string"},
        # "suitability": {"type": "object"},
        "can_be_managed_by_third_party_operator": {"type": "boolean"},
        "is_managed_by_third_party_operator": {"type": "boolean"},
        "third_party_operator": {"type": "object"},
        "is_cvm_qualified_investor": {"type": "boolean"},
        "us_person": {"type": "object"},
    },
    "required": [
        "name",
        "marital",
        "cpf",
        "email",
 #       "suitability",
        "can_be_managed_by_third_party_operator",
        "is_managed_by_third_party_operator",
        "third_party_operator",
        "is_cvm_qualified_investor",
        "us_person",
    ],
}

marital_schema = {
    "type": "object",
    "properties": {"status": {"type": "string"}, "spouse": {"type": "object"}},
    "required": ["status", "spouse"],
    "dependencies": {
        "status": {
            "properties": {"spouse": {"type": "object"}},
            "required": ["spouse"],
        },
        "spouse": {
            "properties": {"status": {"type": "string"}},
            "required": ["status"],
        },
    },
}

spouse = {
    "type": "object",
    "properties": {
        "spouse_name": {"type": "string"},
        "nationality": {"type": "string"},
        "cpf": {"type": "integer"},
    },
    "required": ["spouse_name", "nationality", "cpf"],
}

dtvm_suitability_schema = {
    "type": "object",
    "properties": {
        "score": {"type": "integer"},
        "profile": {"type": "string"},
        "version": {"type": "integer"},
        "done_time_stamp": {"type": "integer"},
    },
    "required": ["score", "profile", "version", "done_time_stamp"],
}

third_party_operator = {
    "type": "object",
    "properties": {
        "is_third_party_operator": {"type": "boolean"},
        "details": {"type": "object"},
        "third_party_operator_email": {"type": "string"},
    },
    "required": ["is_third_party_operator", "details", "third_party_operator_email"],
}

us_person = {
    "type": "object",
    "properties": {
        "is_us_person": {"type": "boolean"},
        "us_tin": {"type": "string"},
    },
    "required": ["is_us_person", "us_tin"],
}

detail_schema = {"type": "object", "properties": {}}

provided_by_bureaux_schema = {
    "type": "object",
    "properties": {
        "gender": {"type": "object"},
        "birthDate": {"type": "object"},
        "naturalness": {"type": "object"},
        "nationality": {"type": "object"},
        "mother_name": {"type": "object"},
        "identifier_document": {"type": "object"},
        "address": {"type": "object"},
        "occupation": {"type": "object"},
        "assets": {"type": "object"},
        "education": {"type": "object"},
        "documents_photos": {"type": "object"},
        "politically_exposed_person": {"type": "object"},
        "date_of_acquisition": {"type": "object"},
    },
    "required": [
        "gender",
        "birthDate",
        "naturalness",
        "nationality",
        "mother_name",
        "identifier_document",
        "address",
        "occupation",
        "assets",
        "education",
        "documents_photos",
        "politically_exposed_person",
        "date_of_acquisition",
    ],
}

string_provided_by_bureaux = {
    "type": "object",
    "properties": {"value": {"type": "string"}, "source": {"type": "string"}},
    "required": ["value", "source"],
}

integer_provided_by_bureaux = {
    "type": "object",
    "properties": {"value": {"type": "integer"}, "source": {"type": "string"}},
    "required": ["value", "source"],
}

number_provided_by_bureaux = {
    "type": "object",
    "properties": {"value": {"type": "number"}, "source": {"type": "string"}},
    "required": ["value", "source"],
}

boolean_provided_by_bureaux = {
    "type": "object",
    "properties": {"value": {"type": "boolean"}, "source": {"type": "string"}},
    "required": ["value", "source"],
}

document_data_schema = {
    "type": "object",
    "properties": {
        "document_data": {
            "number": {"type": "string"},
            "date": {"type": "integer"},
            "state": {"type": "string"},
            "issuer": {"type": "string"},
        }
    },
    "required": ["number", "date", "state", "issuer"],
}

identifier_document_schema = {
    "type": "object",
    "properties": {"type": {"type": "string"}, "document_data": {"type": "object"}},
    "required": ["type", "document_data"],
}

address_schema = {
    "type": "object",
    "properties": {
        "street_name": {"type": "object"},
        "number": {"type": "object"},
        "state": {"type": "object"},
        "city": {"type": "object"},
        "zipCode": {"type": "object"},
        "phone_number": {"type": "object"},
    },
    "required": ["street_name", "number", "state", "city", "zipCode", "phone_number"],
}

occupation_schema = {
    "type": "object",
    "properties": {"status": {"type": "object"}, "company": {"type": "object"}},
    "required": ["status"],
}

company_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "object"},
        "cpnj": {"type": "object"},
    },
    "required": ["name", "cpnj"],
}

assets_schema = {
    "type": "object",
    "properties": {"patrimony": {"type": "number"}, "income": {"type": "number"}},
    "required": ["patrimony", "income"],
}

education_schema = {
    "type": "object",
    "properties": {
        "level": {"type": "object"},
        "course": {"type": "object"},
    },
    "required": ["level"],
}

documents_photos_schema = {
    "type": "object",
    "properties": {
        "identifier_document": {"type": "object"},
        "address_document": {"type": "object"},
    },
    "required": ["identifier_document", "address_document"],
}

politically_exposed_person_schema = {
    "type": "object",
    "properties": {"is_politically_exposed_person": {"type": "object"}},
    "required": ["is_politically_exposed_person"],
}
# "DTVM USER SCHEMA"
########################################################################################
# "TERM SCHEMA"
terms_schema = {
    "type": "object",
    "properties": {
        "metadata": {"type": "object"},
        "term_type": {"type": "string"},
        "term_version": {"type": "string"},
        "user_accept": {"type": "boolean"},
        "term_answer_time_stamp": {"type": "integer"}
    },
    "required": [
        "metadata",
        "term_type",
        "term_version",
        "user_accept",
        "term_answer_time_stamp"
    ],
}

terms_metadata_schema = {
    "type": "object",
    "properties": {"user_email": {"type": "string"}},
    "required": ["user_email"],
}
# "TERM SCHEMA"
########################################################################################
# Prospect User
prospect_user_schema = {
    "type": "object",
    "properties": {
        "user_email": {"type": "string"},
        "name": {"type": "string"},
        "create_user_time_stamp": {"type": "integer"},
    },
    "required": ["user_email", "name", "create_user_time_stamp"],
}
# Prospect User
########################################################################################
# Suitability
suitability_schema = {
    "type": "object",
    "properties": {
        "metadata": {"type": "object"},
        "form": {"type": "array", "items": {
            "oneOf": [
                {
                    "type": "object",
                    "properties": {
                        "question_id": {"type": "integer"},
                        "answer": {"type": "string"}
                    }, "required": [
                        "question_id",
                        "answer"
                        ]
                }
            ]
        }
    },
        "version": {"type": "integer"},
        "score": {"type": "number"},
        "profile": {"type": "string"},
        "create_suitability_time_stamp": {"type": "integer"}
    },
    "required": [
        "metadata",
        "form",
        "version",
        "score",
        "profile",
        "create_suitability_time_stamp"
    ],
}

metadata_suitability_schema = {
    "type": "object",
    "properties": {"user_email": {"type": "string"}},
    "required": ["user_email"],
}

suitability_form_schema = {
    "type": "object",
    "properties": {},
    "required": [],
}
# Suitability
########################################################################################
# DTVM UPDATE USER
dtvm_update_user_schema = {
    "type": "object",
    "properties": {
        "metadata": {"type": "object"},
        "updated_user_data": {"type": "object"},
        "validate_user_time_stamp": {"type": "integer"},
    },
    "required": ["metadata", "updated_user_data", "validate_user_time_stamp"],
}

dtvm_update_user_metadata_schema = {
    "type": "object",
    "properties": {
        "user_email": {"type": "string"},
        "digital_signature_time_stamp": {"type": "integer"},
    },
    "required": ["user_email", "digital_signature_time_stamp"],
}

dtvm_update_user_data_schema = {"type": "object", "properties": {}, "required": []}

dtvm_update_user_street_name_schema = {
    "type": "object",
    "properties": {
        "previous_data": {"type": "string"},
        "new_data": {"type": "string"},
    },
    "required": ["previous_data", "new_data"],
}

dtvm_update_string_field = {
    "type": "object",
    "properties": {
        "previous_data": {"type": "string"},
        "new_data": {"type": "string"},
    },
    "required": ["previous_data", "new_data"],
}

dtvm_update_integer_field = {
    "properties": {
        "previous_data": {"type": "integer"},
        "new_data": {"type": "integer"},
    },
    "required": ["previous_data", "new_data"],
}

dtvm_update_float_field = {
    "type": "object",
    "properties": {
        "previous_data": {"type": "number"},
        "new_data": {"type": "number"},
    },
    "required": ["previous_data", "new_data"],
}

dtvm_update_boolean_field = {
    "type": "object",
    "properties": {
        "previous_data": {"type": "boolean"},
        "new_data": {"type": "boolean"},
    },
    "required": ["previous_data", "new_data"],
}
# DTVM UPDATE USER
########################################################################################
# TABLE
table_schema = {
    "type": "object",
    "properties": {
        "stone_age_id": {"type": "string"},
        "user_id": {"type": "string"},
        "status": {"type": "string"},
        "cpf": {"type": "number"},
    },
    "required": ["stone_age_id", "user_id", "status", "cpf"],
}
# TABLE
schemas = {
    "dtvm_user_schema": {
        "root": dtvm_user_schema,
        "root.metadata": user_metadata_schema,
        "root.user_registry_data": user_registry_schema,
        "root.user_registry_data.provided_by_user": provided_by_user_schema,
        "root.user_registry_data.provided_by_user.marital": marital_schema,
        "root.user_registry_data.provided_by_user.marital.spouse": spouse,
       # "root.user_registry_data.provided_by_user.suitability": dtvm_suitability_schema,
        "root.user_registry_data.provided_by_user.third_party_operator": third_party_operator,
        "root.user_registry_data.provided_by_user.third_party_operator.details": detail_schema,
        "root.user_registry_data.provided_by_user.us_person": us_person,
        "root.user_registry_data.provided_by_bureaux": provided_by_bureaux_schema,
        "root.user_registry_data.provided_by_bureaux.gender": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.birthDate": integer_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.naturalness": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.nationality": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.mother_name": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.identifier_document": identifier_document_schema,
        "root.user_registry_data.provided_by_bureaux.identifier_document.type": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.identifier_document.document_data": document_data_schema,
        "root.user_registry_data.provided_by_bureaux.identifier_document.document_data.number": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.identifier_document.document_data.date": integer_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.identifier_document.document_data.state": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.identifier_document.document_data.issuer": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.address": address_schema,
        "root.user_registry_data.provided_by_bureaux.address.street_name": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.address.number": integer_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.address.state": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.address.city": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.address.zipCode": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.address.phone_number": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.occupation": occupation_schema,
        "root.user_registry_data.provided_by_bureaux.occupation.status": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.occupation.company": company_schema,
        "root.user_registry_data.provided_by_bureaux.occupation.company.name": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.occupation.company.cpnj": integer_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.assets": assets_schema,
        "root.user_registry_data.provided_by_bureaux.assets.patrimony": number_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.assets.income": number_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.education": education_schema,
        "root.user_registry_data.provided_by_bureaux.education.level": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.education.course": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.documents_photos": documents_photos_schema,
        "root.user_registry_data.provided_by_bureaux.documents_photos.identifier_document": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.documents_photos.address_document": string_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.politically_exposed_person": politically_exposed_person_schema,
        "root.user_registry_data.provided_by_bureaux.politically_exposed_person.is_politically_exposed_person": boolean_provided_by_bureaux,
        "root.user_registry_data.provided_by_bureaux.date_of_acquisition": integer_provided_by_bureaux,
    },
    "term_schema": {
        "root": terms_schema,
        "root.metadata": terms_metadata_schema,
    },
    "prospect_user_schema": {"root": prospect_user_schema},
    "suitability_schema": {
        "root": suitability_schema,
        "root.metadata": metadata_suitability_schema,
    },
    "dtvm_update_user_schema": {
        "root": dtvm_update_user_schema,
        "root.metadata": dtvm_update_user_metadata_schema,
        "root.updated_user_data.name": dtvm_update_string_field,
        "root.updated_user_data.address.street_name": dtvm_update_string_field,
        "root.updated_user_data.address.number": dtvm_update_integer_field,
        "root.updated_user_data.address.state": dtvm_update_string_field,
        "root.updated_user_data.address.city": dtvm_update_string_field,
        "root.updated_user_data.address.zipCode": dtvm_update_string_field,
        "root.updated_user_data.address.phone_number": dtvm_update_string_field,
        "root.updated_user_data.marital.status": dtvm_update_string_field,
        "root.updated_user_data.marital.spouse.spouse_name": dtvm_update_string_field,
        "root.updated_user_data.marital.spouse.nationality": dtvm_update_string_field,
        "root.updated_user_data.marital.spouse.cpf": dtvm_update_integer_field,
        "root.updated_user_data.suitability.score": dtvm_update_float_field,
        "root.updated_user_data.suitability.profile": dtvm_update_string_field,
        "root.updated_user_data.suitability.version": dtvm_update_integer_field,
        "root.updated_user_data.suitability.done_time_stamp": dtvm_update_integer_field,
        "root.updated_user_data.is_cvm_qualified_investor": dtvm_update_boolean_field,
        "root.updated_user_data.gender": dtvm_update_string_field,
        "root.updated_user_data.identifier_document.type": dtvm_update_string_field,
        "root.updated_user_data.identifier_document.document_data.number": dtvm_update_string_field,
        "root.updated_user_data.identifier_document.document_data.date": dtvm_update_integer_field,
        "root.updated_user_data.identifier_document.document_data.state": dtvm_update_string_field,
        "root.updated_user_data.identifier_document.document_data.issuer": dtvm_update_string_field,
        "root.updated_user_data.occupation.status": dtvm_update_string_field,
        "root.updated_user_data.occupation.company.name": dtvm_update_string_field,
        "root.updated_user_data.occupation.company.cpnj": dtvm_update_integer_field,
        "root.updated_user_data.assets.patrimony": dtvm_update_float_field,
        "root.updated_user_data.assets.income": dtvm_update_float_field,
        "root.updated_user_data.education.level": dtvm_update_string_field,
        "root.updated_user_data.assets.course": dtvm_update_string_field,
        "root.updated_user_data.documents_photos.address_document": dtvm_update_string_field,
        "root.updated_user_data.documents_photos.identifier_document": dtvm_update_string_field,
        "root.updated_user_data.politically_exposed_person.is_politically_exposed_person": dtvm_update_boolean_field,
    },
    "table_schema": {"root": table_schema},
}
