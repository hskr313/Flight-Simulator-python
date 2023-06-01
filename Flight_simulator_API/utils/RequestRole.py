import json
from functools import wraps
from flask import request, jsonify


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            user = request.headers.get('current_user')

            if user is None:
                return jsonify({'message': 'No user provided'}), 401

            user = json.loads(user)

            if not any(role in roles for role in user.get('roles', [])):
                return jsonify({'message': 'Unauthorized'}), 403

            return f(*args, **kwargs)

        return wrapped

    return wrapper
