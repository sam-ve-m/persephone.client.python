from abc import ABC, abstractmethod


class IBuilderValidator(ABC):
    @classmethod
    @abstractmethod
    def check(cls, payload: dict, dict_schemas: dict):

        pass
