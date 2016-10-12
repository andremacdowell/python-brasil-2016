# encoding:utf-8
from flask import Flask
from routes import my_blueprint

app = Flask(__name__)

# register our blueprints
app.register_blueprint(my_blueprint, url_prefix='/api/v1')
