# encoding: utf-8

MOCK_QUERY_RESULT = "QUERY_RESULT"


def mock_connection(execution_function=lambda x, y: None,
                    fetch_function=lambda x: None):

    cursor = type('cursor', (object, ), {
        'execute': execution_function,
        'fetchall': fetch_function
    })

    def cursor_call(*args, **kwargs):
        return cursor()

    connection = type('connection', (object, ), {
        'cursor': cursor_call,
        'json': lambda x: {},
        'close': lambda x: {},
    })

    return connection()
