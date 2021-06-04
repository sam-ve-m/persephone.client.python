from abc import ABC, abstractmethod


class ISchemaValidator(ABC):

    @classmethod
    @abstractmethod
    def schema_validator(cls, validator: any, payload: dict, schema: dict) -> bool:

        pass

