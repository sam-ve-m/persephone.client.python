from persephone_client.services.queue_producer.service import QueueProducerService


class QueueProducerController:

    @classmethod
    def send_to_queue(cls, producer: any, topic: str, partition: int, msg: dict) -> None:
        QueueProducerService.send_to_queue(producer=producer, topic=topic, partition=partition, msg=msg)
