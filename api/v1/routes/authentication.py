
# Imports
from flask import request
from flask_restx import Namespace, Resource, fields
from api.utils.ressources import PlainTextResource

# API documentation init
api = Namespace('login', description='API authentication')

# Model for Authentication post
model = api.model('Login', {
    'username': fields.String(description="Your username."),
    'password': fields.String(description="Your password."),
})


@api.route('')
class Authentication(Resource, PlainTextResource):

    @api.doc(body=model,
             responses={
                 200: 'Success',
                 400: 'Validation Error'
             })
    def post(self):
        """
        Login to the API.
        Return a confirmation message with your username and the length of your password.
        """

        # If a JSON is send, return a Success message.
        if content := request.get_json():
            message = f"Login success for user {content['username']} " \
                      f"with password from length: {len(content['password'])}!"

            return self.plain_text_response(message, 200)
