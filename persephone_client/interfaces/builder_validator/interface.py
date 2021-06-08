from abc import ABC, abstractmethod


class IBuilderValidator(ABC):
    @classmethod
    @abstractmethod
    def check(cls, payload: dict, schema_key: str):

        pass
