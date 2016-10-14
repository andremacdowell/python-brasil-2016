# encoding: utf-8
import unittest
import redis
import mock
import custom_exceptions
from redis_connector import RedisConnector

mock_config = {
    "host": "localhost",
    "port": 5000,
    "db": 0
}


class TestRedisConnector(unittest.TestCase):

    def setUp(self):
        self.connector = RedisConnector(mock_config)

    @mock.patch('redis.StrictRedis')
    def test_valid_get(self, mock_redis):
        result = self.connector.get('test')
        self.assertIsNotNone(result)

    @mock.patch.object(redis.StrictRedis, 'set')
    def test_valid_set(self, mock_set):
        self.connector.set('test', '123')
        mock_set.assert_called_with('test', '123')

    @mock.patch.object(redis.StrictRedis, 'get')
    @mock.patch.object(redis.StrictRedis, 'keys')
    def test_valid_retrieve_db(self, mock_keys, mock_get):
        mock_get.return_value = "value"
        mock_keys.return_value = ["1", "2"]
        result = self.connector.retrieve_whole_db()
        self.assertEquals(result, [{"1": "value"}, {"2": "value"}])

    @mock.patch('redis.StrictRedis')
    def test_failed_get(self, mock_redis):
        mock_redis.side_effect = [redis.exceptions.ConnectionError()]
        self.assertRaises(custom_exceptions.RedisUnavailable,
                          lambda: self.connector.get('test'))
