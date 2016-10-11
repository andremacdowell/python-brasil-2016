# encoding: utf-8
import falcon
import mock
from falcon import testing
import resources.hello as hello

FAKE_ROUTE = "/test_hello"


def fake_function(*args):
    return True


class TestFalconHello(testing.TestCase):

    def setUp(self):
        self.api = falcon.API()
        self.api.add_route(FAKE_ROUTE, hello.Hello())

    @mock.patch("falcon.request.Request.get_header", fake_function)
    @mock.patch("authentication._verify_authentication", fake_function)
    def test_valid_get(self):
        response = self.simulate_get(FAKE_ROUTE)
        self.assertEqual(response.status, falcon.HTTP_200)
