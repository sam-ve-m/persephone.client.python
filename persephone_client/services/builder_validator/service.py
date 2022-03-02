from persephone_client.domain.validators.schema_validators import ChooseSchema
from persephone_client.core.builder_validator.interface import IBuilderValidator
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
    def _get_schema(cls, schema_to_use: str):
        exists_schema = ChooseSchema.__dict__['_member_map_'].get(schema_to_use)
        if exists_schema:
            return exists_schema.value

    @classmethod
    def handle_validator(cls, payload: dict, schema_to_use: str, logger: any) -> bool:
        if schema := cls._get_schema(schema_to_use):
            return cls._validate_payload(schema=schema, payload=payload, logger=logger)
        else:
            if logger:
                logger.error(f'Schema {schema_to_use} not exists.', exc_info=True)
            return False
