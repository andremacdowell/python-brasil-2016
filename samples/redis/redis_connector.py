# encoding: utf-8
import redis
from singleton import Singleton


class RedisConnector(object):
    __metaclass__ = Singleton

    def __init__(self, config_params):
        self.pool = redis.ConnectionPool(**config_params)
