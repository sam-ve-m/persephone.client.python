from persephone_client.services.schema_validator.service import SchemaValidatorService
from jsonschema import validate

class SchemaValidatorController:

    @classmethod
    def schema_validator(cls, msg: dict, schema: dict) -> bool:

        return SchemaValidatorService.schema_validator(validator=validate, msg=msg, schema=schema)