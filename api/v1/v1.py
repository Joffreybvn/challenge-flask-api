
# Initialize this package as a Flask blueprint
from flask import Blueprint
from flask_restx import Api

# Import the routes
from api.v1.routes import status_api, auth_api, ml_api

blueprint = Blueprint('v1', __name__)

# Merge the blueprints with the doc
api = Api(blueprint,
          title='coucou mathieu',
          version='1.0',
          description='Demo API made with flask and flask-restX.')

api.add_namespace(status_api)
api.add_namespace(auth_api)
api.add_namespace(ml_api)
