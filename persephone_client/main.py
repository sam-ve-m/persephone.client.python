from persephone_client.controllers.schema_validator.controller import SchemaValidatorController
from persephone_client.controllers.queue_producer.controller import QueueProducerController
from kafka import KafkaProducer


class Persephone:

    def __init__(self, host: str, port: int):
        self.producer = KafkaProducer(bootstrap_servers=f'{host}:{port}')

    def run(self, topic: str, partition: int, msg: dict, schema: dict) -> bool:

        if self._validate(msg=msg, schema=schema):
            QueueProducerController.send_to_queue(producer=self.producer, topic=topic, partition=partition, msg=msg)
            return True
        else:
            return False

    @staticmethod
    def _validate(msg: dict, schema: dict) -> bool:
        return SchemaValidatorController.schema_validator(msg=msg, schema=schema)
