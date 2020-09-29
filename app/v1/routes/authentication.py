
# Imports
from flask import request
from flask_restx import Namespace, Resource

# API documentation init
api = Namespace('login', description='Login route')


@api.route('')
class Status(Resource):

    def post(self):
        content = request.get_json()
        return f"Login success for user {content['username']} with password from length: {content['password']}!"
