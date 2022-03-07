# from persephone_client.controllers.schema_validator.controller import SchemaValidatorController
# import pytest
#
#
# def test_invalid_message_as_empty_str():
#     payload = ""
#     schema = "TableSchema"
#     with pytest.raises(Exception, match="Given message must be dict type"):
#         SchemaValidatorController.schema_validator(payload=payload, schema_to_use=schema, logger='')
#
#
# def test_invalid_message_as_empty_byte():
#     payload = b""
#     schema = "TableSchema"
#     with pytest.raises(Exception, match="Given message must be dict type"):
#         SchemaValidatorController.schema_validator(payload=payload, schema_to_use=schema, logger='')
#
#
# def test_invalid_message_as_str():
#     payload = "test message"
#     schema = "TableSchema"
#     with pytest.raises(Exception, match="Given message must be dict type"):
#         SchemaValidatorController.schema_validator(payload=payload, schema_to_use=schema, logger='')
#
#
# def test_invalid_message_as_byte():
#     payload = b"test message"
#     schema = "TableSchema"
#     with pytest.raises(Exception, match="Given message must be dict type"):
#         SchemaValidatorController.schema_validator(payload=payload, schema_to_use=schema, logger='')
#
#
# def test_invalid_message_as_empty_dict():
#     payload = {}
#     schema = "TableSchema"
#     with pytest.raises(Exception, match="Given message must not be empty"):
#         SchemaValidatorController.schema_validator(payload=payload, schema_to_use=schema, logger='')
#
#
# def test_invalid_schema_as_empty_str():
#     payload = {
#         "stone_age_id": 'teste',
#         "user_id": "teste",
#         "status": "teste",
#         "cpf": 129192
#     }
#     schema = ""
#     with pytest.raises(Exception, match="Given message must not be empty"):
#         SchemaValidatorController.schema_validator(payload=payload, schema_to_use=schema, logger='')
#
#
# def test_invalid_schema_as_empty_byte():
#     payload = {
#         "stone_age_id": 'teste',
#         "user_id": "teste",
#         "status": "teste",
#         "cpf": 129192
#     }
#     schema = b""
#     with pytest.raises(Exception, match="Given message must not be empty"):
#         SchemaValidatorController.schema_validator(payload=payload, schema_to_use=schema, logger='')
#
#
# def test_invalid_schema_as_integer():
#     payload = {
#         "stone_age_id": 'teste',
#         "user_id": "teste",
#         "status": "teste",
#         "cpf": 129192
#     }
#     schema = 12345
#     with pytest.raises(Exception, match="Given schema_to_use must be str type"):
#         SchemaValidatorController.schema_validator(payload=payload, schema_to_use=schema, logger='')
#
#
# def test_invalid_schema_as_byte():
#     payload = {
#         "stone_age_id": 'teste',
#         "user_id": "teste",
#         "status": "teste",
#         "cpf": 129192
#     }
#     schema = b"1234"
#     with pytest.raises(Exception, match="Given schema_to_use must be str type"):
#         SchemaValidatorController.schema_validator(payload=payload, schema_to_use=schema, logger='')
#
#
# def test_validate():
#     payload = {
#         "stone_age_id": 'teste',
#         "user_id": "teste",
#         "status": "teste",
#         "cpf": 129192
#     }
#     schema = "TableSchema"
#     assert SchemaValidatorController.schema_validator(payload=payload, schema_to_use=schema, logger='') is True
