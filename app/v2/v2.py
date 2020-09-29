
# Initialize this package as a Flask blueprint
from flask import Blueprint
from flask_restx import Api

# Import the routes
from app.v2.routes import index_api

blueprint = Blueprint('v2', __name__)

# Merge the blueprints with the doc
api = Api(blueprint,
          title='Flask example API',
          version='2.0',
          description='Demo API made with flask and flask-restX.')

api.add_namespace(index_api)
