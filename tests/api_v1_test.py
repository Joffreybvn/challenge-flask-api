
import unittest
import json
from flask import Response

from api.app import create_app


class APIv1TestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_v1_status(self):
        """Unit test for /v1/status"""
        response: Response = self.app.get('/v1/status')

        # Check the status code and data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Alive!')

    def test_v1_login(self):
        """Unit test for /v1/login"""

        # Create the dictionary to send as a JSON
        params = json.dumps({"username": "Foo",
                             "password": "Bar"})

        # Send the POST request
        response = self.app.post('/v1/login',
                                 data=params,
                                 content_type='application/json')

        # Check the status code and data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Login success for user Foo with password from length: 3!')

    def test_v1_predict(self):
        """Unit test for /v1/predict"""

        # Create the dictionary of params
        query = dict(
            seller_available=20,
            month="october",
            customer_visiting_website=10
        )

        # Send the GET request
        response = self.app.get(f"/v1/predict/{query['seller_available']}/{query['month']}/{query['customer_visiting_website']}")

        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(int(response.data), 5000)
        self.assertGreaterEqual(int(response.data), 2000)


if __name__ == '__main__':
    unittest.main()
