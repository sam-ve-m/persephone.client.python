from typing import Tuple

from persephone_client.domain.enums.status.enum import PersephoneClientStatus
from persephone_client.domain.exceptions.exception import InvalidMessage, InvalidSchemaName, SchemaNotFound
from persephone_client.services.schema_validator.service import SchemaValidatorServiceService
from persephone_client.repositories.persephone.repository import PersephoneRepository
from persephone_client.core.services.persephone.interface import IPersephoneService

from etria_logger import Gladsheim


class PersephoneService(IPersephoneService):

    kafka = PersephoneRepository
    schema_validator = SchemaValidatorServiceService

    @classmethod
    async def send_to_persephone(cls, topic: str, partition: int, message: dict, schema_name: str) -> Tuple[bool, PersephoneClientStatus]:
        is_message_sent = False
        try:
            cls.schema_validator.schema_validator(
                message=message,
                schema_name=schema_name
            )

            is_message_sent = await cls.kafka.send_to_persephone(
                topic=topic,
                partition=partition,
                message=message
            )

            return is_message_sent, PersephoneClientStatus.success.value

        except InvalidMessage as err:
            error_message = f"PersephoneService::send_to_persephone::InvalidMessage"
            Gladsheim.error(msg=error_message, stack_level=err, exc_info=True)
            return is_message_sent, PersephoneClientStatus.invalid_message.value

        except InvalidSchemaName as err:
            error_message = f"PersephoneService::send_to_persephone::InvalidSchemaName"
            Gladsheim.error(msg=error_message, stack_level=err, exc_info=True)
            return is_message_sent, PersephoneClientStatus.invalid_schema_name.value

        except SchemaNotFound as err:
            error_message = f"PersephoneService::send_to_persephone::SchemaNotFound"
            Gladsheim.error(msg=error_message, stack_level=err, exc_info=True)
            return is_message_sent, PersephoneClientStatus.schema_not_found.value

        except Exception as err:
            error_message = f"PersephoneService::send_to_persephone::Exception"
            Gladsheim.error(msg=error_message, stack_level=err, exc_info=True)
            return is_message_sent, PersephoneClientStatus.not_mapped_error.value
