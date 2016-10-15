# encoding: utf-8
import unittest
import json
import mock
import flask_restful
from flask import Flask
from resources.hello import Hello

FAKE_ROUTE = "/test_hello"


def mock_response(status_code):
    response = type('response', (object, ), {
        'status_code': status_code,
        'json': lambda x: {}
    })

    return response()


class TestFlaskHello(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = flask_restful.Api(self.app)
        self.api.add_resource(Hello, FAKE_ROUTE)
        self.api.init_app(self.app)

    # Esse teste não é de unidade!!
    def test_that_is_actually_not_an_unit_test(self):
        with self.app.test_client() as client:
            result = client.get(FAKE_ROUTE)
            json_result = json.loads(result.get_data())
            self.assertEquals(result.status_code, 200)
            self.assertTrue(json_result["success"])

    @mock.patch("requests.get", lambda x: mock_response(200))
    def test_that_is_an_unit_test(self):
        with self.app.test_client() as client:
            result = client.get(FAKE_ROUTE)
            json_result = json.loads(result.get_data())

            self.assertEquals(result.status_code, 200)
            self.assertTrue(json_result["success"])
            self.assertEquals(json_result["data"], {})

    @mock.patch("requests.get", lambda x: mock_response(400))
    def test_mock_failure(self):
        with self.app.test_client() as client:
            result = client.get(FAKE_ROUTE)
            json_result = json.loads(result.get_data())

            self.assertEquals(result.status_code, 400)
            self.assertFalse(json_result["success"])
            self.assertEquals(json_result["data"], None)
