
# Imports
from flask_restx import Namespace, Resource, fields

# API documentation init
api = Namespace('status', description='General API information')

# Model for Authentication get
model = api.model('Status', {
    'is_online': fields.Boolean(description="True if the API server is online."),
    'message': fields.String(description="User friendly server status message."),
})


@api.route('/')
class Status(Resource):

    @api.response(200, "Success", model)
    def get(self):
        """
        Return the API server status.
        Return a JSON with the current status of this API.
        """

        return {
            'is_online': True,
            'message': 'The v2 API server is alive.'
        }, 200
