# encoding: utf-8
import falcon
import mock
import json
from falcon import testing
# mock.patch('authentication.authenticate', lambda x, y, z: True).start()
import resources.hello as hello

FAKE_ROUTE = "/test_hello"


def mock_request_class():
    stream = type('stream', (object, ), {
        'read': lambda x: False,
    })

    request = type('request', (object, ), {
        'stream': stream(),
        'get_header': lambda x, y: True
    })

    return request


class TestFalconHello(testing.TestCase):

    def setUp(self):
        self.api = falcon.API()
        self.api.add_route(FAKE_ROUTE, hello.Hello())

    @mock.patch("falcon.request.Request.get_header", lambda x, y: True)
    @mock.patch("authentication._verify_authentication", lambda x: True)
    def test_valid_get(self):
        response = self.simulate_get(FAKE_ROUTE)
        self.assertEqual(response.status, falcon.HTTP_200)

    @mock.patch("falcon.request.Request.get_header", lambda x, y: True)
    @mock.patch("authentication._verify_authentication", lambda x: True)
    def test_valid_post(self):
        body = {"test": "test"}

        response = self.simulate_post(FAKE_ROUTE, body=json.dumps(body))
        self.assertEqual(response.status, falcon.HTTP_202)

        response_dict = json.loads(response.content)
        self.assertEqual(response_dict.get("data"), body)

    @mock.patch("falcon.request.Request.get_header", lambda x, y: True)
    @mock.patch("authentication._verify_authentication", lambda x: True)
    def test_invalid_empty_post(self):
        response = self.simulate_post(FAKE_ROUTE, body=None)
        self.assertEqual(response.status, falcon.HTTP_400)

    @mock.patch("falcon.request.Request.get_header", lambda x, y: True)
    @mock.patch("authentication._verify_authentication", lambda x: True)
    def test_invalid_post(self):
        response = self.simulate_post(FAKE_ROUTE, body="garbage")
        self.assertEqual(response.status, falcon.HTTP_422)
