from persephone_client.interfaces.queue_producer.interface import IQueueProducer
from json import dumps


class QueueProducerService(IQueueProducer):
    @classmethod
    def send_to_queue(
        cls, producer: any, topic: str, partition: int, payload: dict
    ) -> None:
        if type(payload) != dict:
            raise Exception("Given message must be dict type")
        if type(payload) == dict and len(payload) < 1:
            raise Exception("Given message must not be empty")
        try:
            producer.send(
                topic=topic,
                partition=partition,
                value=dumps(payload).encode(),
            )
        except Exception as err:
            raise Exception("Something went wrong when sending to kafka queue")
