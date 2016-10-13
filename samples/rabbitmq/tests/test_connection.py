# encoding: utf-8
import unittest
import pika
from mock import patch
from mqconnection import MQConnection
from custom_exceptions import (
    NoConnectionToMQ, InvalidCredentialsError, UnknownMQError,
    InsufficientPermissionsError, RouteNotFoundError)
from . import mock_config


def mock_connection_class(publish):
    connection = type('connection', (object, ), {
        'channel': lambda x: mock_channel(publish),
        'is_closed': False
    })

    return lambda x: connection()


def mock_channel(publish):
    channel = type('channel', (object, ), {
        'basic_publish': publish,
    })
    return channel()


def failed_publish(*args, **kwargs):
    raise Exception()


def failed_unknown_channel(*args, **kwargs):
    raise pika.exceptions.ChannelClosed()


def failed_permissions_channel(*args, **kwargs):
    exception = pika.exceptions.ChannelClosed()
    exception.args = (403, "")
    raise exception


def failed_route_channel(*args, **kwargs):
    exception = pika.exceptions.ChannelClosed()
    exception.args = (404, "")
    raise exception


def failed_unknown_status_channel(*args, **kwargs):
    exception = pika.exceptions.ChannelClosed()
    exception.args = (500, "")
    raise exception


class TestMQConnection(unittest.TestCase):

    def setUp(self):
        self.mq_connection = MQConnection(**mock_config)

    def tearDown(self):
        self.mq_connection.dispatch()

    @patch('pika.BlockingConnection')
    def test_valid_open_connection(self, mock_pika_conn):
        self.mq_connection.open()
        self.assertIsNotNone(self.mq_connection.connection)

    @patch('pika.BlockingConnection')
    def test_error_connection_closed(self, mock_pika_conn):
        mock_pika_conn.side_effect = [pika.exceptions.ConnectionClosed()]
        self.assertRaises(NoConnectionToMQ, self.mq_connection.open)

    @patch('pika.BlockingConnection')
    def test_error_authentication(self, mock_pika_conn):
        mock_pika_conn.side_effect = [
            pika.exceptions.ProbableAuthenticationError()]
        self.assertRaises(InvalidCredentialsError, self.mq_connection.open)

    @patch('pika.BlockingConnection')
    def test_error_unknown_mq(self, mock_pika_conn):
        mock_pika_conn.side_effect = [Exception()]
        self.assertRaises(UnknownMQError, self.mq_connection.open)

    @patch('pika.BlockingConnection')
    def test_valid_publish(self, mock_pika_conn):
        channel = self.mq_connection.create_channel()
        self.mq_connection.publish_in(
            route='test', channel=channel, body='test')

    @patch(
        'pika.BlockingConnection', mock_connection_class(failed_publish))
    def test_unknown_error(self):
        channel = self.mq_connection.create_channel()
        self.assertRaises(
            UnknownMQError,
            lambda: self.mq_connection.publish_in(
                route='test', channel=channel, body='test'))

    @patch(
        'pika.BlockingConnection',
        mock_connection_class(failed_unknown_channel))
    def test_unknown_channel_closed_error(self):
        channel = self.mq_connection.create_channel()
        self.assertRaises(
            UnknownMQError,
            lambda: self.mq_connection.publish_in(
                route='test', channel=channel, body='test'))

    @patch(
        'pika.BlockingConnection',
        mock_connection_class(failed_permissions_channel))
    def test_permissions_channel_closed_error(self):
        channel = self.mq_connection.create_channel()
        self.assertRaises(
            InsufficientPermissionsError,
            lambda: self.mq_connection.publish_in(
                route='test', channel=channel, body='test'))

    @patch(
        'pika.BlockingConnection',
        mock_connection_class(failed_route_channel))
    def test_route_channel_closed_error(self):
        channel = self.mq_connection.create_channel()
        self.assertRaises(
            RouteNotFoundError,
            lambda: self.mq_connection.publish_in(
                route='test', channel=channel, body='test'))

    @patch(
        'pika.BlockingConnection',
        mock_connection_class(failed_unknown_status_channel))
    def test_unknown_status_channel_closed_error(self):
        channel = self.mq_connection.create_channel()
        self.assertRaises(
            UnknownMQError,
            lambda: self.mq_connection.publish_in(
                route='test', channel=channel, body='test'))
