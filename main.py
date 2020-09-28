
# Imports
from app import create_app

# Initialize the Flask application
app = create_app()


# Run the app
if __name__ == '__main__':
    app.run("127.0.0.1", port=5000, debug=True)
