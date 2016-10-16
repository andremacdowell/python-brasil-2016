# encoding: utf-8
import unittest
import run
import falcon
import mock


class TestRunFunction(unittest.TestCase):

    @mock.patch('falcon.api.API.add_route')
    def test_add_routes(self, mock_add_route):
        routes = run.routes()
        self.assertIsInstance(routes, falcon.api.API)
        self.assertEquals(mock_add_route.call_count, 1)

    @mock.patch('tornado.platform.epoll.EPollIOLoop.start')
    def test_execute_server(self, mock_ioloop_start):
        mock_routes = mock.Mock()
        run.execute(mock_routes)
        self.assertEquals(mock_ioloop_start.call_count, 1)
