from typing import Tuple

from persephone_client.domain.enums.status.enum import PersephoneClientStatus
from persephone_client.services.persephone.service import PersephoneService


class Persephone:

    def __init__(self, bootstrap_servers: str):
        self.bootstrap_servers = bootstrap_servers

    async def send_to_persephone(self, topic: str, partition: int, message: dict, schema_name: str) -> Tuple[bool, PersephoneClientStatus]:
        is_message_sent, persephone_client = PersephoneService.send_to_persephone(
            bootstrap_servers=self.bootstrap_servers,
            topic=topic,
            partition=partition,
            message=message,
            schema_name=schema_name
        )

        return is_message_sent, persephone_client


if __name__ == '__main__':
    pass
