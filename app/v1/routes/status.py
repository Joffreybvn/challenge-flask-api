
# Imports
from flask_restx import Namespace, Resource

# API documentation init
api = Namespace('status', description='General API information')


@api.route('')
class Status(Resource):

    def get(self):
        return "Alive!"
