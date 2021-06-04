from persephone_client.interfaces.schema_validator.interface import ISchemaValidator
from persephone_client.services.builder_validator.service import BuilderValidator


class SchemaValidatorService(ISchemaValidator):

    @classmethod
    def schema_validator(cls, validator: any, payload: dict, schema_list: list) -> bool:
        if type(payload) != dict:
            raise Exception("Given message must be dict type")
        if type(payload) == dict and len(payload) < 1:
            raise Exception("Given message must not be empty")

        if type(schema_list) != list:
            raise Exception("Given message must be dict type")
        if type(schema_list) == list and len(schema_list) < 1:
            raise Exception("Given message must not be empty")

        try:
            BuilderValidator.check(validator=validator, payload=payload, schema_list=schema_list)
            return True
        except:
            return False