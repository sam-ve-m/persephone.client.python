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
        "stone_age_id": 'teste',
        "user_id": "teste",
        "status": "teste",
        "cpf": 129192
    }

    a = Persephone._validate(payload=dic, schema='TableSchema', logger='')

    print(a)
