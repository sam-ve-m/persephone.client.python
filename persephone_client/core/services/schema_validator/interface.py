from abc import ABC, abstractmethod


class ISchemaValidatorService(ABC):

    @staticmethod
    @abstractmethod
    def schema_validator(message: dict, schema_to_use: str):
        pass
