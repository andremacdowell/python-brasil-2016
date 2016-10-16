# encoding: utf-8
import unittest
import run
from run import PORT
import mock


class TestRunFunction(unittest.TestCase):

    @mock.patch('flask.Flask.run')
    def test_execute_production_server(self, mock_flask_run):
        run.execute(False)
        mock_flask_run.assert_called_with(
            host="0.0.0.0", port=PORT, debug=False)

    @mock.patch('flask.Flask.run')
    def test_execute_debug_server(self, mock_flask_run):
        run.execute(True)
        mock_flask_run.assert_called_with(
            host="0.0.0.0", port=PORT, debug=True)
