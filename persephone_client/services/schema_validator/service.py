from persephone_client.core.services.schema_validator.interface import ISchemaValidatorService
from persephone_client.domain.exceptions.exception import InvalidMessage, InvalidSchemaName
from persephone_client.services.message_validator.service import MessageValidatorService
from nidavellir.src.uru import Sindri


class SchemaValidatorServiceService(ISchemaValidatorService):

    @staticmethod
    def __validate_message(message: dict):
        if type(message) != dict:
            raise InvalidMessage(msg="Given message must be dict type")

        if type(message) == dict and len(message) < 1:
            raise InvalidMessage(msg="Given message must not be empty")

    @staticmethod
    def __validate_schema(schema_name: dict):
        if type(schema_name) != str:
            raise InvalidSchemaName("Given schema name must be str type")

        if not schema_name:
            raise InvalidSchemaName("Given schema name must not be empty")

    @staticmethod
    def schema_validator(message: dict, schema_name: str):
        message = Sindri.dict_to_primitive_types(message)
        is_valid_message = MessageValidatorService.validate_message(message=message, schema_name=schema_name)

        if not is_valid_message:
            raise InvalidMessage(msg=f"Given message must be compatible with schema {schema_name}")
