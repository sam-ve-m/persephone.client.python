from persephone_client.interfaces.schema_validator.interface import ISchemaValidator
from persephone_client.services.builder_validator.service import BuilderValidator
from nidavellir.src.uru import Sindri


class SchemaValidatorService(ISchemaValidator):

    @classmethod
    def schema_validator(
        cls, validator: any, payload: dict, schema_key: str, logger: any
    ) -> bool:
        if type(payload) != dict:
            if logger:
                logger.error("Given message must be dict type", exc_info=True)
            return False
        if type(payload) == dict and len(payload) < 1:
            if logger:
                logger.error("Given message must not be empty", exc_info=True)
            return False
        if type(schema_key) != str:
            if logger:
                logger.error("Given schema_key must be str type",exc_info=True)
            return False
        Sindri.dict_to_primitive_types(payload)
        return BuilderValidator.check(validator=validator, payload=payload, schema_key=schema_key, logger=logger)
