from abc import ABC, abstractmethod


class IPersephoneRepository(ABC):

    @classmethod
    @abstractmethod
    async def send_to_persephone(cls, topic: str, partition: int, message: dict) -> bool:
        pass
