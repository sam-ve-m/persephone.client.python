from persephone_client.main import Persephone
from unittest.mock import MagicMock
import pytest
from kafka.errors import NoBrokersAvailable


class StubbyProducer:
    pass


class StubbyValidator:
    pass


def test_persephone_without_dependency_injection():
    msg = {"key": "test"}
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }

    persephone = Persephone(host="localhost", port=9092)
    assert persephone.run(topic="test", partition=0, msg=msg, schema=schema) is True


def test_persephone_with_dependency_injection_True():
    msg = {"key": "test"}
    schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"}
        }
    }

    persephone = Persephone(host="localhost", port=9092)
    producer = MagicMock(return_value=True)
    validator = MagicMock(return_value=True)
    persephone = persephone.with_dependency_injection(validator=validator, producer=producer)
    assert persephone.run(topic="test", partition=0, msg=msg, schema=schema) is True
