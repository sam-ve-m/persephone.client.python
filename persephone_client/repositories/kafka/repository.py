from logging import Logger

from aiokafka.errors import KafkaTimeoutError, KafkaError

from persephone_client.core.repositories.kafka.interface import IKafkaRepository
from persephone_client.infraestructure.kafka.infraestructure import KafkaInfrastructure


class KafkaRepository(IKafkaRepository):

    infra = KafkaInfrastructure

    @classmethod
    def send_to_persephone(cls, bootstrap_servers: str, topic: str, partition: str, message: dict, logger: Logger) -> str:
        is_message_sent = False

        try:
            kafka_consumer = cls.infra.get_or_create_producer(bootstrap_servers)
            send_future = await kafka_consumer.send(topic=topic,partition=partition, message=message)
            is_message_sent = await send_future
        except KafkaTimeoutError as err:
            message = f"KafkaRepository::send_to_persephone::KafkaTimeoutError::is_message_sent:{is_message_sent}"
            logger.error(msg=message, stacklevel=err, exc_info=True)

        except KafkaError as err:
            message = f"KafkaRepository::send_to_persephone::KafkaError::is_message_sent:{is_message_sent}"
            logger.error(msg=message, stacklevel=err, exc_info=True)

        except Exception as err:
            message = f"KafkaRepository::send_to_persephone::Exception::is_message_sent:{is_message_sent}"
            logger.error(msg=message, stacklevel=err, exc_info=True)
