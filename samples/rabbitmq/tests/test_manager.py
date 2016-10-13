# encoding: utf-8
import unittest
from mock import Mock, patch
from mqmanager import MQManager
from . import mock_config


def mock_channel(connection):
    method = type('method', (object, ), {'delivery_tag': 'mock_delivery_tag'})

    channel = type('channel', (object, ), {
        'basic_get': lambda self, queue: (method, "", ""),
        'basic_ack': lambda self, delivery_tag: None
    })
    return channel()


mock_routes = {
    "default": "default_queue",
    "error": "error_queue",
}


class TestMQManager(unittest.TestCase):

    def setUp(self):
        self.mq_manager = MQManager(
            None, mock_config, mock_routes)
        self.mq_manager.initialize()

    @patch('mqconnection.MQConnection.create_channel', mock_channel)
    def test_consume_calls_callback(self):
        mock_callback = Mock()
        self.mq_manager.consumer_callback = mock_callback
        self.mq_manager.consume(single_message=True)

        self.assertTrue(mock_callback.called)

    @patch('mqconnection.MQConnection.create_channel', mock_channel)
    def test_publish_error_route_success(self):
        mock_success_publish = Mock()
        self.mq_manager.connection.publish_in = mock_success_publish
        self.mq_manager.publish_error('test')

        self.assertTrue(mock_success_publish.called)

    @patch('mqconnection.MQConnection.create_channel', mock_channel)
    def test_publish_success(self):
        mock_success_publish = Mock()
        self.mq_manager.connection.publish_in = mock_success_publish
        self.mq_manager.publish(message='test', route='test')

        self.assertTrue(mock_success_publish.called)
