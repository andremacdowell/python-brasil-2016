# encoding: utf-8
import unittest
import mock
import pymssql
from mssqlconnector import MSSQLConnector


class TestMssqlConnector(unittest.TestCase):

    def setUp(self):
        self.test_connector = MSSQLConnector()

    @mock.patch("pymssql.connect")
    def test_connection_interface_error(self, mock_connect):
        mock_connect.side_effect = pymssql.InterfaceError()

        self.assertRaises(pymssql.InterfaceError,
                          self.test_connector.get_connection)

    @mock.patch("pymssql.connect")
    def test_connection_successful(self, mock_raw_connect):
        connection = self.test_connector.get_connection()
        self.assertIsNotNone(connection)

    def test_string_connector(self):
        self.assertEquals(
            str(self.test_connector),
            "{} - {}".format(self.test_connector.server,
                             self.test_connector.user))
