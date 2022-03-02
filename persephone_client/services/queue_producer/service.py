from persephone_client.core.queue_producer.interface import IQueueProducer
from json import dumps
from typing import Optional
from nidavellir.src.uru import Sindri

from persephone_client.repositories.kafka.repository import KafkaRepository


class QueueProducerService(IQueueProducer):

    kafka = KafkaRepository

    @classmethod
    def send_to_queue(cls, bootstrap_servers: str, topic: str, partition: int, payload: dict, logger: any) -> Optional[bool]:
        if type(payload) != dict:
            if logger:
                logger.error("Given message must be dict type", exc_info=True)
            raise Exception('Given message must be dict type')

        if type(payload) == dict and len(payload) < 1:
            if logger:
                logger.error("Given message must not be empty", exc_info=True)
            raise Exception('Given message must not be empty')

        try:
            cls.kafka.send_to_persephone(topic=topic, partition=partition, vlue=dumps(payload, default=Sindri.).encode())
        except Exception as err:
            if logger:
                logger.error(err, exc_info=True)
            return False
