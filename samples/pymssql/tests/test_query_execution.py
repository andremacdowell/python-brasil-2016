# encoding: utf-8
import unittest
import mock
import pymssql
from mssqlconnector import MSSQLConnector

MOCK_QUERY_RESULT = "QUERY_RESULT"


def mock_connection(execution_function):

    cursor = type('cursor', (object, ), {
        'execute': execution_function
    })

    def cursor_call(*args, **kwargs):
        return cursor()

    connection = type('connection', (object, ), {
        'cursor': cursor_call,
        'json': lambda x: {},
        'close': lambda x: {},
    })

    return connection()


class TestMssqlConnector(unittest.TestCase):

    def setUp(self):
        self.test_connector = MSSQLConnector()

    @mock.patch("pymssql.connect")
    def test_operational_failed_execution(self, mock_connect):
        execution_function = mock.MagicMock()
        execution_function.side_effect = [pymssql.OperationalError()]
        mock_connect.return_value = mock_connection(execution_function)
        self.assertRaises(pymssql.OperationalError,
                          lambda: self.test_connector.execute(""))

    @mock.patch("pymssql.connect")
    def test_interface_error_succeds_on_retry(self, mock_connect):
        execution_function = mock.MagicMock(return_value=MOCK_QUERY_RESULT)
        execution_function.side_effect = [pymssql.InterfaceError(),
                                          lambda: {}]
        mock_connect.return_value = mock_connection(execution_function)
        cursor = self.test_connector.execute("")
        self.assertIsNotNone(cursor)

    @mock.patch("pymssql.connect")
    def test_unknown_error_failed_execution(self, mock_connect):
        execution_function = mock.MagicMock(return_value=MOCK_QUERY_RESULT)
        execution_function.side_effect = [pymssql.ProgrammingError()]
        mock_connect.return_value = mock_connection(execution_function)
        self.assertRaises(Exception,
                          lambda: self.test_connector.execute(""))

    @mock.patch("pymssql.connect")
    def test_success_execution(self, mock_connect):
        mock_connect.return_value = mock_connection(
            lambda x, y: MOCK_QUERY_RESULT)
        cursor = self.test_connector.execute("")
        self.assertIsNotNone(cursor)
