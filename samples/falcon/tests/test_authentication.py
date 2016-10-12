# encoding: utf-8
import falcon
from falcon import testing
from resources.hello import Hello
from authentication import VALID

FAKE_ROUTE = "/test_authentication"
INVALID = "garbage"


class TestAuthentication(testing.TestCase):

    def setUp(self):
        self.api = falcon.API()
        self.api.add_route(FAKE_ROUTE, Hello())

    def test_valid_get(self):
        response = self.simulate_get(
            FAKE_ROUTE, headers={"token": VALID})
        self.assertEqual(response.status, falcon.HTTP_200)

    def test_invalid_get(self):
        response = self.simulate_get(
            FAKE_ROUTE, headers={"token": INVALID})
        self.assertEqual(response.status, falcon.HTTP_401)
