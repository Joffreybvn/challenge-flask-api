
# Imports
from flask import request
from flask_restx import Namespace, Resource, fields

# API documentation init
api = Namespace('login', description='API authentication')

# Model for Authentication post
model = api.model('Login', {
    'username': fields.String(description="Your username."),
    'password': fields.String(description="Your password."),
})


@api.route('')
class Authentication(Resource):

    @api.doc(id='get_something',
             body=model,
             responses={
                 200: 'Success',
                 400: 'Validation Error'
             })
    def post(self):
        """
        Login to the API.
        Return a confirmation message with your username and the length of your password.
        """

        content = request.get_json()
        return f"Login success for user {content['username']} with password from length: {len(content['password'])}!"
