
from flask import make_response


class PlainTextResource:

    @staticmethod
    def plain_text_response(text: str, status_code: int):

        # Create a plain text response
        response = make_response(text, status_code)
        response.mimetype = "text/plain"

        return response
