from abc import ABC, abstractmethod


class IPersephoneService(ABC):
    @classmethod
    @abstractmethod
    def send_to_persephone(cls, producer: any, topic: str, partition: int, message: dict, schema: str) -> None:
        pass
