from persephone_client.controllers.schema_validator.controller import (
    SchemaValidatorController,
)
from persephone_client.controllers.queue_producer.controller import (
    QueueProducerController,
)
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
            self.producer = KafkaProducer(bootstrap_servers=f"{self.host}:{self.port}")
            self.validator = validate
        except NoBrokersAvailable:
            raise Exception(
                "I need an instance of kafka server to finish my log registry"
            )

    def with_dependency_injection(self, validator: any, producer: any):
        self.validator = validator
        self.producer = producer
        return Persephone(host=self.host, port=self.port)

    def run(
        self, topic: str, partition: int, payload: dict, dict_schemas: dict
    ) -> bool:
        if self._validate(
            validator=self.validator, payload=payload, dict_schemas=dict_schemas
        ):
            QueueProducerController.send_to_queue(
                producer=self.producer,
                topic=topic,
                partition=partition,
                payload=payload,
            )
            return True

        return False

    @staticmethod
    def _validate(validator: any, payload: dict, dict_schemas: dict) -> bool:
        return SchemaValidatorController.schema_validator(
            validator=validator, payload=payload, dict_schemas=dict_schemas
        )
