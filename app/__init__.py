
from flask_restx import Api
from flask import Flask
from config import Config

# App blueprint imports
from app.v1 import blueprint as blueprint_v1
from app.v2 import blueprint as blueprint_v2


def create_app(config_class=Config):

    # Initialize the Flask server
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Load the blueprints
    app.register_blueprint(blueprint_v1, url_prefix='/v1')
    app.register_blueprint(blueprint_v2, url_prefix='/v2')

    return app
