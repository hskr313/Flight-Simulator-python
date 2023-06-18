import json
from functools import wraps
from flask import request, jsonify
from JsonHelpers.UserHelper import UserHelper


def requires_roles(*roles):
    """
    Decorator to ensure the current user has at least one of the specified roles. This is used for route
    authorization in a Flask application. If the user doesn't have the required role, a 403 Unauthorized response is
    returned.

    :param roles: The roles required to access the decorated function.
    :return: Wrapper function.
    """

    def wrapper(f):
        """
        Inner function that wraps the decorated function.

        :param f: The decorated function.
        :return: Wrapped function.
        """

        @wraps(f)
        def wrapped(*args, **kwargs):
            """
            The actual wrapper function that gets called when the decorated function is called. It checks the role of
            the user before proceeding.

            :param args: Positional arguments passed to the decorated function. :param kwargs: Keyword arguments
            passed to the decorated function. :return: Result of the decorated function, or a JSON response
            indicating an error if user's role is not authorized.
            """
            user = request.headers.get("Authorization")

            if user is None:
                return jsonify({"message": "No user provided"}), 401

            user = json.loads(user)

            if not any(role in roles for role in user.get("roles", [])):
                return jsonify({"message": "Unauthorized"}), 403

            return f(*args, **kwargs)

        return wrapped

    return wrapper
