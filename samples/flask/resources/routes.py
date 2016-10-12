# encoding: utf-8
import flask_restful as restful
from flask import Blueprint
from unipath import Path
from hello import Hello

PATH = str(Path(__file__).parent.parent.parent.child('csv'))

my_blueprint = Blueprint('zendesk_apps', __name__)
api = restful.Api()
api.init_app(my_blueprint)

api.add_resource(Hello, '/hello')
