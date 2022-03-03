from persephone_client.core.repositories.persephone.interface import IPersephoneRepository
from persephone_client.infraestructure.kafka.infraestructure import KafkaInfrastructure

from etria_logger import Gladsheim
from nidavellir import Sindri


from aiokafka.errors import KafkaTimeoutError, KafkaError
from orjson import dumps


class PersephoneRepository(IPersephoneRepository):

    infra = KafkaInfrastructure

    @classmethod
    def send_to_persephone(cls, bootstrap_servers: str, topic: str, partition: int, message: dict) -> bool:
        is_message_sent = False

        try:
            kafka_consumer = cls.infra.get_or_create_producer(bootstrap_servers)
            dumps(message, default=Sindri.dict_to_primitive_types)

            send_future = await kafka_consumer.send(topic=topic,partition=partition, message=message)
            is_message_sent = await send_future

        except KafkaTimeoutError as err:
            message = f"KafkaRepository::send_to_persephone::KafkaTimeoutError::is_message_sent:{is_message_sent}"
            Gladsheim.error(msg=message, stacklevel=err, exc_info=True)

        except KafkaError as err:
            message = f"KafkaRepository::send_to_persephone::KafkaError::is_message_sent:{is_message_sent}"
            Gladsheim.error(msg=message, stacklevel=err, exc_info=True)

        except Exception as err:
            message = f"KafkaRepository::send_to_persephone::Exception::is_message_sent:{is_message_sent}"
            Gladsheim.error(msg=message, stacklevel=err, exc_info=True)

        return is_message_sent
