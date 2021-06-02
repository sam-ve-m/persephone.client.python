from abc import ABC, abstractmethod


class ISchemaValidator(ABC):

    @classmethod
    @abstractmethod
    def schema_validator(cls, validator: any, msg: dict, schema: dict) -> bool:

        pass
