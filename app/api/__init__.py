
# Initialize this package as a Flask blueprint
from flask import Blueprint
bp = Blueprint('api', __name__)

# Import later to avoid circular dependency errors.
from app.api import authentication, machine_learning  # , errors
