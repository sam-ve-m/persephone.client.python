from persephone_client.main import Persephone
from unittest.mock import MagicMock
import pytest
from kafka.errors import NoBrokersAvailable


class StubbyProducer:
    pass


class StubbyValidator:
    pass


def test_persephone_without_dependency_injection():
    payload = {"key": "test"}
    schema = {"type": "object", "properties": {"key": {"type": "string"}}}

    persephone = Persephone(host="localhost", port=9092)
    assert (
        persephone.run(topic="test", partition=0, payload=payload, schema=schema)
        is True
    )


def test_persephone_with_dependency_injection_True():
    payload = {
        "stone_age_id": 'teste',
        "user_id": "teste",
        "status": "teste",
        "cpf": 129192
    }
    schema = "TableSchema"

    persephone = Persephone(host="localhost", port=9092)
    producer = MagicMock(return_value=True)
    persephone = persephone.with_dependency_injection(producer=producer)
    assert (persephone.run(topic="test", partition=0, payload=payload, schema=schema) is True)
