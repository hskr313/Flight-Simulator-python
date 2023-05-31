from flask import Blueprint, request, jsonify

from JsonHelpers.UserHelper import UserHelper
from mappers.UserMapper import UserMapper
from models.security.SafeUser import SafeUser
from services.UserService import UserService
from services.AuthService import AuthService


class AuthController:
    def __init__(self, user_service: UserService,
                 auth_service: AuthService,
                 user_helper: UserHelper,
                 user_mapper: UserMapper,
                 file_path
                 ):
        self.user_mapper = user_mapper
        self.user_helper = user_helper
        self.user_service = user_service
        self.auth_service = auth_service
        self.file_path = file_path
        self.blueprint = Blueprint("auth", __name__)
        self.blueprint.add_url_rule('/login', 'login', self.login, methods=['POST'])
        self.blueprint.add_url_rule('/register', 'register', self.register, methods=['POST'])

    def register(self):
        data = request.get_json()
        if self.user_service.email_exists(data.get('email')):
            return jsonify({'message': 'Email already registered'}), 400

        if not AuthService.validate_roles(data.get('roles')):
            return jsonify({'message': 'Invalid role'}), 400

        hashed_password = self.auth_service.hash_password(data.get('password'))
        data["password"] = hashed_password

        new_user = self.user_mapper.from_json(data)

        saved_user = self.user_helper.save(new_user, self.file_path)
        safe_user = SafeUser(saved_user).to_json()
        return jsonify(safe_user), 201

    def login(self):
        data = request.get_json()
        user = self.user_service.get_user_by_email(data.get('email'))
        if not user or not self.auth_service.check_password_hash(user.password, data.get('password')):
            return jsonify({'message': 'Invalid email or password'}), 401

        safe_user = SafeUser(user).to_json()
        return jsonify(safe_user), 200
