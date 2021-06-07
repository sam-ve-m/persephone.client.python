from persephone_client.services.schema_validator.service import SchemaValidatorService


class SchemaValidatorController:
    @classmethod
    def schema_validator(
        cls, validator: any, payload: dict, dict_schemas: dict
    ) -> bool:

        return SchemaValidatorService.schema_validator(
            validator=validator, payload=payload, dict_schemas=dict_schemas
        )
