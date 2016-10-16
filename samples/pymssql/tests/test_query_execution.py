# encoding: utf-8
import unittest
import mock
import pymssql
from mssqlconnector import MSSQLConnector
from . import (mock_connection, MOCK_QUERY_RESULT)


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
        fetch_function = mock.MagicMock(return_value=MOCK_QUERY_RESULT)
        mock_connect.return_value = mock_connection(
            fetch_function=fetch_function)
        cursor = self.test_connector.execute("")
        self.assertEquals(cursor.fetchall(), MOCK_QUERY_RESULT)
