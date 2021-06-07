from abc import ABC, abstractmethod


class ISchemaValidator(ABC):
    @classmethod
    @abstractmethod
    def schema_validator(
        cls, validator: any, payload: dict, dict_schemas: dict
    ) -> bool:

        pass
