# encoding: utf-8
import unittest
import pika
from mock import patch
from mqconnection import MQConnection
from custom_exceptions import (
    NoConnectionToMQ, InvalidCredentialsError, UnknownMQError)
from . import mock_config


class TestMQConnection(unittest.TestCase):

    def setUp(self):
        self.mq_connection = MQConnection(**mock_config)

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
