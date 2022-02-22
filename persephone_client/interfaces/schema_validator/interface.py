from abc import ABC, abstractmethod


class ISchemaValidator(ABC):
    @classmethod
    @abstractmethod
    def schema_validator(cls, payload: dict, schema_to_use: str, logger: any) -> bool:
        pass
