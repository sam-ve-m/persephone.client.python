from persephone_client.controllers.schema_validator.controller import SchemaValidatorController
from persephone_client.controllers.queue_producer.controller import QueueProducerController
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
from jsonschema import validate


class Persephone:
    host = None
    port = None

    def __init__(self, host: str, port: int) -> None:
        try:
            self.host = host
            self.port = port
            self.producer = KafkaProducer(bootstrap_servers=f'{self.host}:{self.port}')
            self.validator = validate
        except NoBrokersAvailable:
            raise Exception("I need an instance of kafka server to finish my log registry")

    def with_dependency_injection(self, validator: any, producer: any):
        self.validator = validator
        self.producer = producer
        return Persephone(host=self.host, port=self.port)

    def run(self, topic: str, partition: int, msg: dict, schema: dict) -> bool:
        if self._validate(validator=self.validator, msg=msg, schema=schema):
            QueueProducerController.send_to_queue(producer=self.producer, topic=topic, partition=partition, msg=msg)
            return True
        else:
            return False

    @staticmethod
    def _validate(validator: any, msg: dict, schema: dict) -> bool:
        return SchemaValidatorController.schema_validator(validator=validator, msg=msg, schema=schema)
