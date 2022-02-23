from persephone_client.controllers.schema_validator.controller import SchemaValidatorController
from persephone_client.controllers.queue_producer.controller import QueueProducerController
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable


class Persephone:
    host = None
    port = None

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

    def with_dependency_injection(self, producer: any):
        self.producer = producer
        return Persephone(host=self.host, port=self.port, logger=self.logger)

    def run(self, topic: str, partition: int, payload: dict, schema: str) -> bool:
        if self.producer is None:
            return False
        if self._validate(payload=payload, schema=schema, logger=self.logger):
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
    def _validate(payload: dict, schema: str, logger: any) -> bool:
        return SchemaValidatorController.schema_validator(payload=payload, schema_to_use=schema, logger=logger)


if __name__ == '__main__':
    dic = {
        'unique_id': 'dbfffc8d-a57e-4156-95da-bde8bbaa78d3',
        'previous_electronic_signature': 'ea73ced01f94d96f7f46682055d6e3915b626a2ebbf98818a09ea2efb6af1a9e',
        'previous_is_blocked_electronic_signature': False,
        'previous_electronic_signature_wrong_attempts': 0,
        'new_electronic_signature': 'ea73ced01f94d96f7f46682055d6e3915b626a2ebbf98818a09ea2efb6af1a9e',
        'new_is_blocked_electronic_signature': False,
        'new_electronic_signature_wrong_attempts': 0}


    print(Persephone._validate(payload=dic, schema='user_change_or_reset_electronic_signature_schema', logger=''))