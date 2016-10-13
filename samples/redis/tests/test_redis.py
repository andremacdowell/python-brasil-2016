# encoding: utf-8
import unittest
from redis_connector import RedisConnector

mock_config = {
    "host": "localhost",
    "port": 5000,
    "db": 0
}


class TestRedisConnector(unittest.TestCase):

    def setUp(self):
        self.connector = RedisConnector(**mock_config)

    def test_something(self):
        pass
