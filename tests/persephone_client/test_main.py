from persephone_client.main import Persephone
from unittest.mock import MagicMock


class StubbyProducer:
    pass


class StubbyValidator:
    pass


def test_persephone_without_dependency_injection():
    payload = {
        "stone_age_id": 'teste',
        "user_id": "teste",
        "status": "teste",
        "cpf": 129192
    }
    schema = "TableSchema"

    persephone = Persephone(host="localhost", port=9092)
    assert persephone.run(topic="test", partition=0, payload=payload, schema=schema) is True


def test_persephone_with_dependency_injection_true():
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
    assert persephone.run(topic="test", partition=0, payload=payload, schema=schema) is True
