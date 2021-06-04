from persephone_client.services.schema_validator.service import SchemaValidatorService


class SchemaValidatorController:

    @classmethod
    def schema_validator(cls, validator: any, payload: dict, schema_list: list) -> bool:

        return SchemaValidatorService.schema_validator(validator=validator, payload=payload, schema=schema_list)
