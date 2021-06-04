from persephone_client.interfaces.builder_validator.interface import IBuilderValidator


class BuilderValidator(IBuilderValidator):

    @staticmethod
    def _chupeta(payload: dict, schema_list: list, key: str = "base"):

        BuilderValidator.validator(payload, schema_list[key])
        for key, property_value in payload.items():
            is_object = type(property_value) is dict
            if is_object:
                BuilderValidator.chupeta(property_value, schema_list, key)

            is_dict_property_list = type(property_value) is list
            if is_dict_property_list:
                for list_value in property_value:
                    BuilderValidator.chupeta(list_value, schema_list, key)

    @classmethod
    def check(cls, validator: any, payload: dict, schema_list: list):
        cls._chupeta(validator=validator, payload=payload, schema_list=schema_list)