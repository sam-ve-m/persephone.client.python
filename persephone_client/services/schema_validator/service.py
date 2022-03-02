from persephone_client.core.schema_validator import ISchemaValidator
from persephone_client.services.builder_validator.service import BuilderValidator
from nidavellir.src.uru import Sindri


class SchemaValidatorService(ISchemaValidator):
    @classmethod
    def schema_validator(cls, payload: dict, schema_to_use: str, logger: any) -> bool:
        if type(payload) != dict:
            if logger:
                logger.error("Given message must be dict type", exc_info=True)
            raise Exception("Given message must be dict type")

        if type(payload) == dict and len(payload) < 1:
            if logger:
                logger.error("Given message must not be empty", exc_info=True)
            raise Exception("Given message must not be empty")

        if not schema_to_use:
            if logger:
                logger.error("Given message must not be empty", exc_info=True)
            raise Exception("Given message must not be empty")

        if type(schema_to_use) != str:
            if logger:
                logger.error("Given schema_to_use must be str type", exc_info=True)
            raise Exception("Given schema_to_use must be str type")

        Sindri.dict_to_primitive_types(payload)
        return BuilderValidator.handle_validator(payload=payload, schema_to_use=schema_to_use, logger=logger)
