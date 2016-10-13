# encoding: utf-8
import redis
import json
import custom_exceptions
from singleton import Singleton


class RedisConnector(object):

    __metaclass__ = Singleton

    def __init__(self, config_params):
        self.pool = redis.ConnectionPool(**config_params)

    def get(self, key):
        sr = self._get_strict_redis()
        return sr.get(key)

    def set(self, key, value):
        sr = self._get_strict_redis()
        return sr.set(key, value)

    def retrieve_whole_db(self, db):
        sr = self._get_strict_redis()
        value = map(lambda x: {x: json.loads(sr.get(x))},
                    sr.keys())
        return value

    def _get_strict_redis(self):
        try:
            sr = redis.StrictRedis(connection_pool=self.pool)
        except redis.exceptions.ConnectionError as e:
            raise custom_exceptions.RedisUnavailable(e)
        return sr
