
# Imports
from flask import request
from flask_restx import Namespace, Resource, fields
import random

# API documentation init
api = Namespace('predict', description='Machine learning routes.')

# Parser for MachineLearning get
parser = api.parser()
parser.add_argument('seller_available', type=int, help='Seller availability', location='path')
parser.add_argument('month', type=str, help='Month to predict for', location='path')
parser.add_argument('customer_visiting_website', type=int, help='Number of customers visiting the website', location='path')


@api.route('/<int:seller_available>/<string:month>/<int:customer_visiting_website>')
class MachineLearning(Resource):

    @api.doc(responses={
                 200: 'Success',
                 400: 'Validation Error'
             })
    @api.expect(parser)
    def get(self, seller_available, month, customer_visiting_website):
        """
        Return a prediction.
        Return a prediction based on the given parameters.
        """

        return random.randint(2000, 5000)
