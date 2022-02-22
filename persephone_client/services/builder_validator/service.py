from persephone_client.domain.validators.schema_validators import ChooseSchema
from persephone_client.interfaces.builder_validator.interface import IBuilderValidator
from pydantic import ValidationError


class BuilderValidator(IBuilderValidator):
    @classmethod
    def _validate_payload(cls, schema: any, payload: dict, logger: any) -> bool:
        try:
            schema(**payload)
            return True
        except ValidationError as error:
            if logger:
                logger.error(error, exc_info=True)
            return False

    @classmethod
    def _verify_exists_schema(cls, schema_to_use: str):
        exists_schema = schema_to_use in ChooseSchema.schemas
        return exists_schema

    @classmethod
    def handle_validator(cls, payload: dict, schema_to_use: str, logger: any) -> bool:
        if cls._verify_exists_schema(schema_to_use):
            schema = ChooseSchema.schemas[schema_to_use]
            return cls._validate_payload(schema=schema, payload=payload, logger=logger)
        else:
            return False
