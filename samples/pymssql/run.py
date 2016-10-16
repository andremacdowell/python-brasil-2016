# encoding: utf-8
from mssqlconnector import MSSQLConnector
from custom_exceptions import (SQLConnectionError, SQLExecutionError)

QUERY = """
SELECT * TOP 1 FROM DB.TABLE
"""


def execute(sql_query):
    connector = MSSQLConnector()

    # Try and get a connection
    try:
        connection = connector.get_connection()
    except Exception, e:
        raise SQLConnectionError(e)
    print str(connection)

    # Try and make a query
    try:
        rows = connector.execute(sql_query)
    except Exception, e:
        raise SQLExecutionError(e)

    return rows


if __name__ == "__main__":  # pragma: no cover
    print "Result is: ", execute(QUERY)
