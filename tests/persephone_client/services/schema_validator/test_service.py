from persephone_client.controllers.schema_validator.controller import SchemaValidatorController
from unittest.mock import MagicMock
import pytest


def test_invalid_message_as_empty_str():
    msg = ""
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, msg=msg, schema=schema)

def test_invalid_message_as_empty_byte():
    msg = b""
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, msg=msg, schema=schema)

def test_invalid_message_as_str():
    msg = "test message"
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, msg=msg, schema=schema)

def test_invalid_message_as_byte():
    msg = b"test message"
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, msg=msg, schema=schema)

def test_invalid_message_as_empty_dict():
    msg = {}
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must not be empty"):
        SchemaValidatorController.schema_validator(validator, msg=msg, schema=schema)

def test_invalid_schema_as_empty_dict():
    msg = {"key": "test"}
    schema = {}
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must not be empty"):
        SchemaValidatorController.schema_validator(validator, msg=msg, schema=schema)

def test_invalid_schema_as_empty_byte():
    msg = {"key": "test"}
    schema = b""
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, msg=msg, schema=schema)

def test_invalid_schema_as_empty_str():
    msg = {"key": "test"}
    schema = ""
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, msg=msg, schema=schema)

def test_invalid_schema_as_str():
    msg = {"key": "test"}
    schema = "test schema"
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, msg=msg, schema=schema)

def test_invalid_schema_as_byte():
    msg = {"key": "test"}
    schema = b"test schema"
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, msg=msg, schema=schema)

def test_validate():
    msg = {"key": "test"}
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }
    validator = MagicMock(return_value=True)
    assert SchemaValidatorController.schema_validator(validator, msg=msg, schema=schema) is True
