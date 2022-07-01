from typing import Tuple

from persephone_client.domain.enums.status.enum import PersephoneClientStatus
from persephone_client.services.persephone.service import PersephoneService


class Persephone:

    @staticmethod
    async def send_to_persephone(topic: str, partition: int, message: dict, schema_name: str) -> Tuple[bool, PersephoneClientStatus]:
        is_message_sent, persephone_client_status = await PersephoneService.send_to_persephone(
            topic=topic,
            partition=partition,
            message=message,
            schema_name=schema_name
        )

        return is_message_sent, persephone_client_status
