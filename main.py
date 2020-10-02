
# https://flask-restx.readthedocs.io/en/latest/swagger.html
# Imports
from api.app import create_app

api = create_app()


# Run the app
if __name__ == '__main__':
    api.run(port=5000, debug=False, threaded=True)
