from persephone_client.controllers.schema_validator.controller import SchemaValidatorController
from persephone_client.controllers.queue_producer.controller import QueueProducerController
from kafka import KafkaProducer
from jsonschema import validate


class Persephone:

    def __init__(self, host: str, port: int) -> None:
        self.producer = KafkaProducer(bootstrap_servers=f'{host}:{port}')
        self.validator = validate

    @classmethod
    def with_dependency_injection(cls, validator: any, producer: any) -> None:
        return cls(validator=validator, producer=producer)

    def run(self, topic: str, partition: int, msg: dict, schema: dict) -> bool:

        if self._validate(validator=self.validator, msg=msg, schema=schema):
            QueueProducerController.send_to_queue(producer=self.producer, topic=topic, partition=partition, msg=msg)
            return True
        else:
            return False

    @staticmethod
    def _validate(validator: any, msg: dict, schema: dict) -> bool:
        return SchemaValidatorController.schema_validator(validator=validator, msg=msg, schema=schema)
