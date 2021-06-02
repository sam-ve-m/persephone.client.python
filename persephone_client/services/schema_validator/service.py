from persephone_client.interfaces.schema_validator.interface import ISchemaValidator


class SchemaValidatorService(ISchemaValidator):

    @classmethod
    def schema_validator(cls, validator: any, msg: dict, schema: dict) -> bool:
        if type(msg) != dict:
            raise Exception("Given message must be dict type")
        if type(msg) == dict and len(msg) < 1:
            raise Exception("Given message must not be empty")

        if type(schema) != dict:
            raise Exception("Given message must be dict type")
        if type(schema) == dict and len(schema) < 1:
            raise Exception("Given message must not be empty")

        try:
            validator(msg, schema)
            return True
        except:
            return False