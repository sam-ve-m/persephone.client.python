from persephone_client.interfaces.builder_validator.interface import IBuilderValidator
from persephone_client.utils.json_schemas import schemas


class BuilderValidator(IBuilderValidator):

    @classmethod
    def _chupeta(cls, validator: any, payload: dict, dict_schemas: dict, parent_key: str, logger: any) -> bool:

        print(dict_schemas[parent_key])
        exists_schema_property = parent_key in dict_schemas
        if exists_schema_property:
            try:
                print(payload)
                validator.validate(instance=payload, schema=dict_schemas[parent_key])
            except Exception as err:
                if logger:
                    logger.error(err, exc_info=True)
                return False

        for key, property_value in payload.items():
            is_object = type(property_value) is dict
            if is_object:
                three_path = ".".join([parent_key, key])
                BuilderValidator._chupeta(
                    validator=validator,
                    payload=property_value,
                    dict_schemas=dict_schemas,
                    parent_key=three_path,
                    logger=logger
                )

            is_dict_property_list = type(property_value) is list
            if is_dict_property_list:
                for list_value in property_value:
                    BuilderValidator._chupeta(validator=validator,
                        payload=list_value, dict_schemas=dict_schemas, parent_key=key, logger=logger
                    )
        return True

    @classmethod
    def check(cls, validator: any, payload: dict, schema_key: str, logger: any) -> bool:
        return BuilderValidator._chupeta(validator=validator,
            payload=payload, dict_schemas=schemas[schema_key], parent_key="root", logger=logger
        )
