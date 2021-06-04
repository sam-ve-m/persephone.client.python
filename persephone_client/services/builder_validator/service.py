from persephone_client.interfaces.builder_validator.interface import IBuilderValidator


class BuilderValidator(IBuilderValidator):

    def __init__(self, validator: any):
        self.validator = validator

    def _chupeta(self, payload: dict, dict_schemas: dict, parent_key: str) -> bool:

            exists_schema_property = parent_key in dict_schemas
            if exists_schema_property:
                print("exists_schema_property", parent_key)
                print("dict_schemas[key]", dict_schemas[parent_key])
                try:
                    self.validator(payload, dict_schemas[parent_key])
                except Exception as err:
                    raise Exception(err)
                    return False

            for key, property_value in payload.items():
                is_object = type(property_value) is dict
                if is_object:
                    three_path = ".".join([parent_key, key])
                    print("three_path: ", three_path)
                    self._chupeta(payload=property_value, dict_schemas=dict_schemas, parent_key=three_path)

                is_dict_property_list = type(property_value) is list
                if is_dict_property_list:
                    for list_value in property_value:
                        self._chupeta(
                            payload=list_value,
                            dict_schemas=dict_schemas,
                            parent_key=key
                        )
            return True

    def check(self, payload: dict, dict_schemas: dict) -> bool:
        return self._chupeta(payload=payload, dict_schemas=dict_schemas, parent_key="root")
