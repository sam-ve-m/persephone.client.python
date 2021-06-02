from abc import ABC, abstractmethod


class IQueueProducer(ABC):

    @classmethod
    @abstractmethod
    def send_to_queue(cls, producer: any, topic: str, partition: int, msg: dict) -> None:

        pass
