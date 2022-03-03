from abc import ABC, abstractmethod


class IPersephoneRepository(ABC):

    @classmethod
    @abstractmethod
    def send_to_persephone(cls, bootstrap_server: str, topic: str, partition: int, message: dict) -> str:
        pass
