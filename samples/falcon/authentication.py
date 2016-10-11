# encoding: utf-8
import falcon

VALID = 'python-brasil-2016'


def _verify_authentication(token):
    return token == VALID


def authenticate(request, response, resource, params):
    token = request.get_header('token')
    if not token:
        raise falcon.HTTPError(falcon.HTTP_400, 'Error',
                               'Please provide an authentication token.')
    if not _verify_authentication(token):
        raise falcon.HTTPError(falcon.HTTP_401,
                               'Error', 'Invalid or expired token.')
