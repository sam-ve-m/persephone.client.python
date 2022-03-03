from abc import ABC, abstractmethod


class IMessageValidatorService(ABC):
    @staticmethod
    @abstractmethod
    def validate_message(payload: dict, schema_name: str):
        pass
