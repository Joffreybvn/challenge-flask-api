
from flask import request
from app.api import bp


@bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        pass

