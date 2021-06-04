from persephone_client.controllers.schema_validator.controller import SchemaValidatorController
from unittest.mock import MagicMock
import pytest


def test_invalid_message_as_empty_str():
    payload = ""
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, payload=payload, schema=schema)

def test_invalid_message_as_empty_byte():
    payload = b""
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, payload=payload, schema=schema)

def test_invalid_message_as_str():
    payload = "test message"
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, payload=payload, schema=schema)

def test_invalid_message_as_byte():
    payload = b"test message"
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, payload=payload, schema=schema)

def test_invalid_message_as_empty_dict():
    payload = {}
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must not be empty"):
        SchemaValidatorController.schema_validator(validator, payload=payload, schema=schema)

def test_invalid_schema_as_empty_dict():
    payload = {"key": "test"}
    schema = {}
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must not be empty"):
        SchemaValidatorController.schema_validator(validator, payload=payload, schema=schema)

def test_invalid_schema_as_empty_byte():
    payload = {"key": "test"}
    schema = b""
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, payload=payload, schema=schema)

def test_invalid_schema_as_empty_str():
    payload = {"key": "test"}
    schema = ""
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, payload=payload, schema=schema)

def test_invalid_schema_as_str():
    payload = {"key": "test"}
    schema = "test schema"
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, payload=payload, schema=schema)

def test_invalid_schema_as_byte():
    payload = {"key": "test"}
    schema = b"test schema"
    validator = MagicMock(return_value=True)
    with pytest.raises(Exception, match="Given message must be dict type"):
        SchemaValidatorController.schema_validator(validator, payload=payload, schema=schema)

def test_validate():
    payload = {"key": "test"}
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }
    validator = MagicMock(return_value=True)
    assert SchemaValidatorController.schema_validator(validator, payload=payload, schema=schema) is True
