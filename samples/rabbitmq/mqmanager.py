# encoding: utf-8
import json
from bson import json_util
from mqconnection import MQConnection


class MQManager(object):

    def __init__(self, consumer_callback, config_params, routes):
        self.application_key = config_params["appkey"]
        self.rabbitmq_parameters = config_params
        self.routes = routes
        self.consumer_callback = consumer_callback
        self.connection = None
        self.publishing_channel = None

    def initialize(self):
        self.connection = MQConnection(**self.rabbitmq_parameters)

    def consume(self, single_message=False):
        channel = self.connection.create_channel()
        queue = self.routes['default']

        if single_message:
            method, properties, body = channel.basic_get(queue)

            if (method and properties and body) is not None:
                self.callback(channel, method, properties, body)
        else:
            channel.basic_consume(self.callback, queue)
            channel.start_consuming()

    def callback(self, channel, method, properties, body):
        self.consumer_callback(body)
        channel.basic_ack(method.delivery_tag)

    def publish_error(self, message):
        route = self.routes['error']
        self.publish(message=message, route=route)

    def publish(self, message, route):
        if self.publishing_channel is None:
            self.publishing_channel = self.connection.create_channel()

        message_object = {
            'application_key': self.application_key,
            'message': message
        }

        body = json.dumps(message_object, default=json_util.default)
        self.connection.publish_in(
            route=route, channel=self.publishing_channel, body=body)

    def stop(self):
        self.connection.close()
        self.connection = None
