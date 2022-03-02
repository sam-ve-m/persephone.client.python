# Third part
from aiokafka import AIOKafkaProducer


class KafkaInfrastructure:

    producer = None

    @classmethod
    def get_or_create_producer(cls, bootstrap_servers):
        if cls.producer is None:
            cls.producer = AIOKafkaProducer(
                bootstrap_servers=bootstrap_servers,
            )

        return cls.producer
