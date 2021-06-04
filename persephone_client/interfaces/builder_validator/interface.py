from abc import ABC, abstractmethod


class IBuilderValidator(ABC):

    @classmethod
    @abstractmethod
    def check(cls, validator: any, payload: dict, schema_list: list):

        pass