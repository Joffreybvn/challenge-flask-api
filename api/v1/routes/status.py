
# Imports
from flask_restx import Namespace, Resource
from api.utils.ressources import PlainTextResource

# API documentation init
api = Namespace('status', description='General API information')


@api.route('')
class Status(Resource, PlainTextResource):

    @api.response(200, "Success")
    def get(self):
        """
        Return the API server status.
        Return "Alive!" if this API server is online.
        """

        # Return a plain text response
        return self.plain_text_response("Alive!", 200)
