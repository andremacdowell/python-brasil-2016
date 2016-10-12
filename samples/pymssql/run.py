# encoding: utf-8
from mssqlconnector import MSSQLConnector

QUERY = """
SELECT * TOP 1 FROM DB.TABLE
"""


def execute(sql_query):
    connector = MSSQLConnector()

    # Try and get a connection
    try:
        connection = connector.get_connection()
    except Exception, e:
        print "FAILED TO GET CONNECTION: ", str(e)
        return

    # Try and make a query
    try:
        rows = connection.execute(sql_query)
    except Exception, e:
        print "FAILED EXECUTE QUERY: ", str(e)
        return

    return rows


if __name__ == "__main__":
    print "Result is: ", execute(QUERY)
