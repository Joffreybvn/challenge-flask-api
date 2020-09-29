
# Imports
from flask_restx import Namespace, Resource

# API documentation init
api = Namespace('index', description='General API information')


@api.route('/status')
class Status(Resource):

    def get(self):

        return "Alive!"
