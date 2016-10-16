# encoding: utf-8
import unittest
import run
import mock
import custom_exceptions
from . import (mock_connection, MOCK_QUERY_RESULT)


class TestRunFunction(unittest.TestCase):

    @mock.patch('mssqlconnector.MSSQLConnector.get_connection')
    def test_connection_failed(self, mock_connection):
        mock_connection.side_effect = [Exception()]
        self.assertRaises(custom_exceptions.SQLConnectionError,
                          lambda: run.execute(""))

    @mock.patch('pymssql.connect')
    def test_execute_failed(self, mock_connect):
        execution_function = mock.MagicMock(return_value=MOCK_QUERY_RESULT)
        execution_function.side_effect = [Exception()]
        mock_connect.return_value = mock_connection(execution_function)
        self.assertRaises(custom_exceptions.SQLExecutionError,
                          lambda: run.execute(""))

    @mock.patch('pymssql.connect')
    def test_execute_success(self, mock_connect):
        fetch_function = mock.MagicMock(return_value=MOCK_QUERY_RESULT)
        mock_connect.return_value = mock_connection(
            fetch_function=fetch_function)
        cursor = run.execute("")
        self.assertEquals(cursor.fetchall(), MOCK_QUERY_RESULT)
