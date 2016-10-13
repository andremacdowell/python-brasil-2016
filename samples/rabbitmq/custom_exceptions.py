# encoding: utf-8


class InvalidCredentialsError(Exception):
    def __init__(self, exception):
        message = "Could not connect due to invalid credentials. Exception" + \
            " occured: {}".format(str(exception))
        super(InvalidCredentialsError, self).__init__(message)


class UnknownMQError(Exception):
    def __init__(self, exception):
        message = "An unknown MQ Error has occured. Exception occured: " + \
            "{}".format(str(exception))
        super(UnknownMQError, self).__init__(message)


class NoConnectionToMQ(Exception):
    def __init__(self, exception):
        message = "No connection could be estabilished to the MQ. " + \
            "Exception occured: {}".format(str(exception))
        super(NoConnectionToMQ, self).__init__(message)


class RouteNotFoundError(Exception):
    def __init__(self, message):
        message = "The received route does not exist. Message received: " + \
            "{}".format(message)
        super(RouteNotFoundError, self).__init__(message)


class InsufficientPermissionsError(Exception):
    def __init__(self, message):
        message = "Invalid permission to access route. Message received: " + \
            "{}".format(message)
        super(InsufficientPermissionsError, self).__init__(message)
