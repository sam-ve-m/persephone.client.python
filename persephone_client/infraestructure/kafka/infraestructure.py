# Third part
from aiokafka import AIOKafkaProducer

from persephone_client.infraestructure.env_config import config


class KafkaInfrastructure:

    producer = None

    @classmethod
    async def get_or_create_producer(cls):
        if cls.producer is None:
            cls.producer = AIOKafkaProducer(
                bootstrap_servers=config("PERSEPHONE_KAFKA_BROKERS"),
                enable_idempotence=True,
                acks=-1
            )
            await cls.producer.start()

        return cls.producer
