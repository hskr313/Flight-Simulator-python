from flask import Blueprint, request, jsonify

from JsonHelpers.UserHelper import UserHelper
from mappers.AddressMapper import AddressMapper
from mappers.UserMapper import UserMapper
from models.security.SafeUser import SafeUser
from services.UserService import UserService
from services.AuthService import AuthService


class AuthController:
    """
    Controller for authentication. It provides methods for user registration and login.
    """

    def __init__(self, user_service: UserService, auth_service: AuthService):
        """
        Initialize the AuthController with the necessary services.

        :param user_service: Service responsible for user-related operations.
        :param auth_service: Service responsible for authentication-related operations.
        """
    def __init__(self, user_service: UserService, auth_service: AuthService, user_mapper: UserMapper):
        self.user_service = user_service
        self.auth_service = auth_service
        self.user_mapper = user_mapper
        self.blueprint = Blueprint("auth", __name__)
        self.blueprint.add_url_rule('/login', 'login', self.login, methods=['POST'])
        self.blueprint.add_url_rule('/register', 'register', self.register, methods=['POST'])

    def register(self):
        """
        Register a new user based on the provided data. Email must be unique, roles must be valid,
        and password is hashed before storage.

        :return: a JSON response with either an error message or the registered user's data.
        """
        data = request.get_json()

        if self.user_service.email_exists(data.get('email')):
            return jsonify({'message': 'Email already registered'}), 400

        if not AuthService.validate_roles(data.get('roles')):
            return jsonify({'message': 'Invalid role'}), 400

        hashed_password = self.auth_service.hash_password(data.get('password'))
        data["password"] = hashed_password

        new_user = self.user_mapper.from_json(data)

        saved_user = self.user_service.save(new_user)
        safe_user = SafeUser(saved_user).to_json()
        return jsonify(safe_user), 201

    def login(self):
        """
        Log in a user based on the provided email and password.

        :return: a JSON response with either an error message or the logged in user's data.
        """
        data = request.get_json()
        user = self.user_service.get_user_by_email(data.get('email'))
        if not user or not self.auth_service.check_password_hash(user.password, data.get('password')):
            return jsonify({'message': 'Invalid email or password'}), 401

        safe_user = SafeUser(user).to_json()
        return jsonify(safe_user), 200
