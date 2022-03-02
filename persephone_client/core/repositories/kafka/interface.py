from abc import ABC, abstractmethod
from logging import Logger


class IKafkaRepository(ABC):

    @classmethod
    @abstractmethod
    def send_to_persephone(cls, bootstrap_server: str, topic: str, partition: str, message: dict, logger: Logger) -> str:
        pass
