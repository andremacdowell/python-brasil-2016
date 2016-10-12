# encoding: utf-8
import unittest
import mock
from mssqlconnector import MSSQLConnector

# TODO: MOCK & EXECUTE DO CURSOR
# TODO: MOCK DO CLOSE DA CONNECTION


class TestMssqlConnector(unittest.TestCase):

    def setUp(self):
        self.test_connector = MSSQLConnector()

    @mock.patch("pymssql.connect")
    def test_operational_failed_execution(self, mock_connect):
        # TODO
        self.test_connector.execute("")

    @mock.patch("pymssql.connect")
    def test_interface_failed_execution(self, mock_connect):
        # TODO
        self.test_connector.execute("")

    @mock.patch("pymssql.connect")
    def test_retry_with_failed_execution(self, mock_connect):
        # TODO
        self.test_connector.execute("")

    @mock.patch("pymssql.connect")
    def test_retry_with_success_execution(self, mock_connect):
        # TODO
        self.test_connector.execute("")

    @mock.patch("pymssql.connect")
    def test_success_execution(self, mock_connect):
        # TODO
        self.test_connector.execute("")
