# encoding: utf-8
import pymssql


class MSSQLConnector(object):
    conn = None

    def __init__(self):
        self.server = "http://localhost"
        self.user = "very_secret_user"
        self.password = "even_more_secret_pwd"
        self.name = "my_db"
        self.port = 33333

    def __str__(self):
        return lambda x: "{} - {}".format(x.server, x.user)

    def get_connection(self):
        try:
            if not self.conn:
                self.conn = pymssql.connect(
                    server=self.server, user=self.user,
                    password=self.password, port=self.port)
            return self.conn
        except Exception, e:
            print "EXCEPTION: ", e
            raise e

    def close_connection(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute(self, sql, as_dict=True, **kwargs):
        sql = sql.format(**kwargs)
        cursor = None

        try:
            cursor = self.get_connection().cursor(as_dict=as_dict)
            cursor.execute(sql)
            return cursor
        except pymssql.OperationalError, e:
            print "EXCEPTION: ", e
            raise e
        except pymssql.InterfaceError, e:
            print "EXCEPTION: ", e
            cursor = self._retry_execution(sql)
            return cursor
        except Exception, e:
            print "EXCEPTION: ", e
            raise e

    def _set_connection(self):
        self.close_connection()
        return self.get_connection()

    def _retry_execution(self, sql):
        connection = self._set_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor
