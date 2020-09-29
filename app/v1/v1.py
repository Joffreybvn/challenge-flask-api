
# Initialize this package as a Flask blueprint
from flask import Blueprint
from flask_restx import Api

# Import the routes
from app.v1.routes import index_api, auth_api

blueprint = Blueprint('v1', __name__)

# Merge the blueprints with the doc
api = Api(blueprint,
          title='Flask example API',
          version='1.0',
          description='Demo API made with flask and flask-restX.')

api.add_namespace(index_api)
api.add_namespace(auth_api)
