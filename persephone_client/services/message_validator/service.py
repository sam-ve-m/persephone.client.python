from etria_logger import Gladsheim

from persephone_client.domain.exceptions.exception import SchemaNotFound
from persephone_client.domain.enums.schema.enum import ChooseSchema
from persephone_client.core.services.message_validator.interface import IMessageValidatorService
from pydantic import ValidationError


class MessageValidatorService(IMessageValidatorService):

    @staticmethod
    def __apply_schema(schema_to_apply: any, message: dict) -> bool:
        try:
            schema_to_apply(**message)
            return True
        except ValidationError as error:
            Gladsheim.error(error, exc_info=True)
            return False

    @staticmethod
    def __get_schema(schema_to_use: str):
        exists_schema = ChooseSchema.__dict__['_member_map_'].get(schema_to_use)
        return exists_schema

    @staticmethod
    def validate_message(message: dict, schema_name: str) -> bool:
        schema_to_apply = MessageValidatorService.__get_schema(schema_name)
        if not schema_to_apply:
            raise SchemaNotFound(msg=f"Schema {schema_name} not exists.")

        is_valid_message = MessageValidatorService.__apply_schema(schema_to_apply=schema_to_apply.value, message=message)
        return is_valid_message
