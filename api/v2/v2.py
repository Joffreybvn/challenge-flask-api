
# Initialize this package as a Flask blueprint
from flask import Blueprint
from flask_restx import Api

# Import the routes
from api.v2.routes import status_api

blueprint = Blueprint('v2', __name__)

# Merge the blueprints with the doc
api = Api(blueprint,
          title='Flask Demo API',
          version='2.0',
          description='This is a demo API, made with flask.',
          contact='joffreybvn@gmail.com')

api.add_namespace(status_api)
