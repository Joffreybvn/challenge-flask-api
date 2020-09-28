
from flask import Flask
from config import Config

from app.api import bp as blueprint_api

# db = SQLAlchemy()


def create_app(config_class=Config):

    # Initialize the Flask server
    app = Flask(__name__)
    app.config.from_object(config_class)

    # db.init_app(app)
    # migrate.init_app(app, db)

    # Load the blueprints
    app.register_blueprint(blueprint_api, url_prefix='/api')

    return app
