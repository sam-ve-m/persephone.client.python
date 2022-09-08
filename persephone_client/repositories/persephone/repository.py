from persephone_client.core.repositories.persephone.interface import IPersephoneRepository
from persephone_client.infraestructure.kafka.infraestructure import KafkaInfrastructure

from etria_logger import Gladsheim
from nidavellir import Sindri


from aiokafka.errors import KafkaTimeoutError, KafkaError
from orjson import dumps


class PersephoneRepository(IPersephoneRepository):

    infra = KafkaInfrastructure

    @classmethod
    async def send_to_persephone(cls, topic: str, partition: int, message: dict) -> bool:
        is_message_sent = True
        record_metadata = None

        try:
            kafka_producer = await cls.infra.get_or_create_producer()
            message = dumps(message, default=Sindri.dict_to_primitive_types)
            record_metadata = await kafka_producer.send_and_wait(topic=topic, partition=partition, value=message)

        except KafkaTimeoutError as err:
            message = f"KafkaRepository::send_to_persephone::KafkaTimeoutError::is_message_sent:{is_message_sent}::error:{err}"
            is_message_sent = False
            Gladsheim.error(msg=message, stacklevel=err, exc_info=True)

        except (KafkaError, AssertionError) as err:
            message = f"KafkaRepository::send_to_persephone::KafkaError::is_message_sent:{is_message_sent}::error:{err}"
            is_message_sent = False
            Gladsheim.error(msg=message, stacklevel=err, exc_info=True)

        except Exception as err:
            message = f"KafkaRepository::send_to_persephone::Exception::is_message_sent:{is_message_sent}::error:{err}"
            is_message_sent = False
            Gladsheim.error(msg=message, stacklevel=err, exc_info=True)

        return is_message_sent
