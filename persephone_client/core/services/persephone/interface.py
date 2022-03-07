from abc import ABC, abstractmethod
from typing import Tuple

from persephone_client.domain.enums.status.enum import PersephoneClientStatus


class IPersephoneService(ABC):

    @classmethod
    @abstractmethod
    async def send_to_persephone(cls, topic: str, partition: int, message: dict, schema_name: str) -> Tuple[bool, PersephoneClientStatus]:
        pass
