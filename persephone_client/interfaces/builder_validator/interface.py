from abc import ABC, abstractmethod


class IBuilderValidator(ABC):
    @classmethod
    @abstractmethod
    def handle_validator(cls, payload: dict, schema_to_use: str, logger: any):
        pass
