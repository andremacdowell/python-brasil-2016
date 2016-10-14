# encoding: utf-8


class RedisUnavailable(Exception):
    def __init__(self, exception):
        message = "Could not connect to Redis with given configurations. " + \
            "Original exception: {}".format(str(exception))
        super(RedisUnavailable, self).__init__(message)
