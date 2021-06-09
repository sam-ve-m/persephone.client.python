from persephone_client.controllers.schema_validator.controller import (
    SchemaValidatorController,
)
from persephone_client.controllers.queue_producer.controller import (
    QueueProducerController,
)
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import jsonschema


class Persephone:
    host = None
    port = None
    validator = jsonschema

    def __init__(self, host: str, port: int, logger: any = None) -> None:
        try:
            self.host = host
            self.port = port
            self.logger = logger
            self.producer = KafkaProducer(bootstrap_servers=f"{self.host}:{self.port}")
        except NoBrokersAvailable:
            self.producer = None
            if self.logger:
                logger.error("I need an instance of kafka server to finish my log registry", exc_info=True)
                pass

    def with_dependency_injection(self, validator: any, producer: any):
        self.validator = validator
        self.producer = producer
        return Persephone(host=self.host, port=self.port, logger=self.logger)

    def run(
        self, topic: str, partition: int, payload: dict, schema_key: str
    ) -> bool:
        if self.producer is None:
            return False

        if self._validate(
            validator=self.validator, payload=payload, schema_key=schema_key, logger=self.logger
        ):
            QueueProducerController.send_to_queue(
                producer=self.producer,
                topic=topic,
                partition=partition,
                payload=payload,
                logger=self.logger
            )
            return True

        return False

    @staticmethod
    def _validate(validator: any, payload: dict, schema_key: str, logger: any) -> bool:
        return SchemaValidatorController.schema_validator(
            validator=validator, payload=payload, schema_key=schema_key, logger=logger
        )