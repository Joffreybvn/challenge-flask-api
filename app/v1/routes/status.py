
# Imports
from flask_restx import Namespace, Resource

# API documentation init
api = Namespace('status', description='General API information')


@api.route('')
class Status(Resource):

    @api.response(200, "Success")
    def get(self):
        """
        Return the API server status.
        Return "Alive!" if this API server is online.
        """

        return "Alive!"
