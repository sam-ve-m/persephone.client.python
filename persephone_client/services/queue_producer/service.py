from persephone_client.interfaces.queue_producer.interface import IQueueProducer
from json import dumps
from typing import Optional
from nidavellir.src.uru import Sindri


class QueueProducerService(IQueueProducer):
    @classmethod
    def send_to_queue(
            cls, producer: any, topic: str, partition: int, payload: dict, logger: any
    ) -> Optional[bool]:
        if type(payload) != dict:
            if logger:
                logger.error("Given message must be dict type", exc_info=True)
            return False
        if type(payload) == dict and len(payload) < 1:
            if logger:
                logger.error("Given message must not be empty", exc_info=True)
            return False
        try:
            producer.send(
                topic=topic,
                partition=partition,
                value=dumps(payload, cls=Sindri).encode(),
            )
        except Exception as err:
            if logger:
                logger.error(err, exc_info=True)
            return False
