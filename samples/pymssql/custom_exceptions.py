# encoding: utf-8


class SQLConnectionError(Exception):
    def __init__(self, exception):
        message = "Could not connect to the SQL Server with the given " + \
            "configuration. Exception occured: {}".format(str(exception))
        super(SQLConnectionError, self).__init__(message)


class SQLExecutionError(Exception):
    def __init__(self, exception):
        message = "Could not execute given query. Exception occured: " + \
            "{}".format(str(exception))
        super(SQLExecutionError, self).__init__(message)
