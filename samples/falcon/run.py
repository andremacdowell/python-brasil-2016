# encoding: utf-8
import falcon
from tornado import (httpserver, ioloop, wsgi)
from resources.hello import Hello

PORT = 5000


def routes():
    # V1
    routes = falcon.API()
    routes.add_route('/api/v1/hello', Hello())

    return routes


def execute(routes):
    # Servidor WSGI
    container = wsgi.WSGIContainer(routes)
    http_server = httpserver.HTTPServer(container)
    http_server.listen(PORT)
    ioloop.IOLoop.instance().start()


if __name__ == '__main__':  # pragma: no cover
    execute(routes())
