from persephone_client.services.schema_validator.service import SchemaValidatorService


class SchemaValidatorController:

    @classmethod
    def schema_validator(cls, validator: any, msg: dict, schema: dict) -> bool:

        return SchemaValidatorService.schema_validator(validator=validator, msg=msg, schema=schema)
