# encoding: utf-8
import pika
from custom_exceptions import (NoConnectionToMQ, InvalidCredentialsError,
                               UnknownMQError, InsufficientPermissionsError,
                               RouteNotFoundError)


class MQConnection(object):
    def __init__(self, appkey, hostname, port=None, username=None,
                 password=None):

        self.credentials = None
        if username and password is not None:
            self.credentials = pika.PlainCredentials(username, password)

        self.parameters = pika.ConnectionParameters(
            host=hostname,
            port=port,
            credentials=self.credentials)

        self.connection = None

    def open(self):
        try:
            self.connection = pika.BlockingConnection(self.parameters)
        except pika.exceptions.ConnectionClosed as e:
            raise NoConnectionToMQ(exception=e)
        except pika.exceptions.ProbableAuthenticationError as e:
            raise InvalidCredentialsError(exception=e)
        except Exception as e:
            raise UnknownMQError(exception=e)

    def close(self):
        self.connection.close()
        self.connection = None

    def create_channel(self):
        if self.connection is None or self.connection.is_closed:
            self.open()

        return self.connection.channel()

    def publish_in(self, route, channel, body):
        try:
            channel.basic_publish(body=body, exchange=route, routing_key='')
        except pika.exceptions.ChannelClosed as e:
            if len(e.args) == 2:
                status_code = e.args[0]
                message = e.args[1]
                if(status_code == 403):
                    raise InsufficientPermissionsError(message=message)
                elif(status_code == 404):
                    raise RouteNotFoundError(message=message)
                else:
                    raise UnknownMQError(exception=e)
            else:
                raise UnknownMQError(exception=e)
        except Exception as e:
            raise UnknownMQError(exception=e)
