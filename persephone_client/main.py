from persephone_client.services.schema_validator.service import SchemaValidatorService
from persephone_client.services.queue_producer.service import QueueProducerService


class Persephone:

    def __init__(self, bootstrap_servers: str, logger: any = None) -> None:
        self.bootstrap_servers = bootstrap_servers
        self.logger = logger

    async def send_to_persephone(self, topic: str, partition: int, payload: dict, schema: str) -> bool:
        QueueProducerService.send_to_queue(
            bootstrap_servers=self.bootstrap_servers,
            topic=topic,
            partition=partition,
            payload=payload,
            logger=self.logger
        )

        pass
        # if self._validate(payload=payload, schema=schema, logger=self.logger):
        #     QueueProducerService.send_to_queue(
        #         producer=self.producer,
        #         topic=topic,
        #         partition=partition,
        #         payload=payload,
        #         logger=self.logger
        #     )
        #     return True
        #
        # return False

if __name__ == '__main__':
    dic = {
        'unique_id': 'dbfffc8d-a57e-4156-95da-bde8bbaa78d3',
        'previous_electronic_signature': 'ea73ced01f94d96f7f46682055d6e3915b626a2ebbf98818a09ea2efb6af1a9e',
        'previous_is_blocked_electronic_signature': False,
        'previous_electronic_signature_wrong_attempts': 0,
        'new_electronic_signature': 'ea73ced01f94d96f7f46682055d6e3915b626a2ebbf98818a09ea2efb6af1a9e',
        'new_is_blocked_electronic_signature': False,
        'new_electronic_signature_wrong_attempts': 0
    }

    print(Persephone._validate(payload=dic, schema='user_change_or_reset_electronic_signature_schema', logger=''))
