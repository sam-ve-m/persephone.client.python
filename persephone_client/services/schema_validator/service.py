from persephone_client.interfaces.schema_validator.interface import ISchemaValidator
from persephone_client.services.builder_validator.service import BuilderValidator


class SchemaValidatorService(ISchemaValidator):
    @classmethod
    def schema_validator(
        cls, validator: any, payload: dict, schema_key: str
    ) -> bool:
        if type(payload) != dict:
            raise Exception("Given message must be dict type")
        if type(payload) == dict and len(payload) < 1:
            raise Exception("Given message must not be empty")

        if type(schema_key) != str:
            raise Exception("Given schema_key must be str type")

        builder_validator = BuilderValidator(validator=validator)
        return builder_validator.check(payload=payload, schema_key=schema_key)
