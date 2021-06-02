from persephone_client.controllers.queue_producer.controller import QueueProducerController
from unittest.mock import MagicMock
import pytest

class StubbyProducer:

    pass

producer = StubbyProducer()


def test_invalid_message_as_empty_byte():
    producer.send = MagicMock(return_value=True)
    msg = b""
    with pytest.raises(Exception, match="Given message must be dict type"):
        QueueProducerController.send_to_queue(producer=producer, topic="test", partition=0, msg=msg)

def test_invalid_message_as_empty_str():
    producer.send = MagicMock(return_value=True)
    msg = ""
    with pytest.raises(Exception, match="Given message must be dict type"):
        QueueProducerController.send_to_queue(producer=producer, topic="test", partition=0, msg=msg)


def test_invalid_message_as_byte():
    producer.send = MagicMock(return_value=True)
    msg = b"teste messsage"
    with pytest.raises(Exception, match="Given message must be dict type"):
        QueueProducerController.send_to_queue(producer=producer, topic="test", partition=0, msg=msg)

def test_invalid_message_as_str():
    producer.send = MagicMock(return_value=True)
    msg = "teste message"
    with pytest.raises(Exception, match="Given message must be dict type"):
        QueueProducerController.send_to_queue(producer=producer, topic="test", partition=0, msg=msg)

def test_invalid_message_as_byte():
    producer.send = MagicMock(return_value=True)
    msg = b"teste messsage"
    with pytest.raises(Exception, match="Given message must be dict type"):
        QueueProducerController.send_to_queue(producer=producer, topic="test", partition=0, msg=msg)

def test_invalid_message_as_str():
    producer.send = MagicMock(return_value=True)
    msg = "teste message"
    with pytest.raises(Exception, match="Given message must be dict type"):
        QueueProducerController.send_to_queue(producer=producer, topic="test", partition=0, msg=msg)



def test_invalid_message_as_dict_empty():
    producer.send = MagicMock(return_value=True)
    msg = {}
    with pytest.raises(Exception, match="Given message must not be empty"):
        QueueProducerController.send_to_queue(producer=producer, topic="test", partition=0, msg=msg)

def test_invalid_message_as_dict_valid():
    producer.send = MagicMock(return_value=True)
    msg = {"key": "value"}
    assert QueueProducerController.send_to_queue(producer=producer, topic="test", partition=0, msg=msg) is None
