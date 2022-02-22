from persephone_client.services.schema_validator.service import SchemaValidatorService


class SchemaValidatorController:
    @classmethod
    def schema_validator(cls, payload: dict, schema_to_use: str, logger: any) -> bool:
        return SchemaValidatorService.schema_validator(payload=payload, schema_to_use=schema_to_use, logger=logger)
