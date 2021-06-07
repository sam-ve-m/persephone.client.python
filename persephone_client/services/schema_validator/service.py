from persephone_client.interfaces.schema_validator.interface import ISchemaValidator
from persephone_client.services.builder_validator.service import BuilderValidator


class SchemaValidatorService(ISchemaValidator):
    @classmethod
    def schema_validator(
        cls, validator: any, payload: dict, dict_schemas: dict
    ) -> bool:
        if type(payload) != dict:
            raise Exception("Given message must be dict type")
        if type(payload) == dict and len(payload) < 1:
            raise Exception("Given message must not be empty")

        if type(dict_schemas) != dict:
            raise Exception("Given dict_schema must be dict type")
        if type(dict_schemas) == list and len(dict_schemas) < 1:
            raise Exception("Given dict_schema must not be empty")

        builder_validator = BuilderValidator(validator=validator)
        return builder_validator.check(payload=payload, dict_schemas=dict_schemas)

