from flask_bcrypt import Bcrypt
from flask import request, jsonify

from mappers.UserMapper import UserMapper
from models.security.SafeUser import SafeUser


class AuthService:
    def __init__(self, user_service):
        self.bcrypt = Bcrypt()
        self.user_service = user_service

    def hash_password(self, password) -> str:
        return self.bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password_hash(self, hashed_password, password) -> bool:
        return self.bcrypt.check_password_hash(hashed_password, password)

    @staticmethod
    def validate_roles(roles) -> bool:
        allowed_roles = ["USER", "PILOT"]
        return all(role in allowed_roles for role in roles)
