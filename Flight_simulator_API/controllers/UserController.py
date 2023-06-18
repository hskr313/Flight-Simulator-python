from flask import Blueprint, request, jsonify

from services.UserService import UserService
from utils.RequestRole import requires_roles


class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service
        self.blueprint = Blueprint("users", __name__)
        self.blueprint.add_url_rule("/users", "get_all", self.get_all, methods=["GET"])
        self.blueprint.add_url_rule(
            "/user/<int:user_id>", "get_one_by_id", self.get_one_by_id, methods=["GET"]
        )
        self.blueprint.add_url_rule(
            "/users", "create_user", self.save_user, methods=["POST"]
        )
        self.blueprint.add_url_rule(
            "/user/<int:user_id>", "update_user", self.save_user, methods=["PUT"]
        )
        self.blueprint.add_url_rule(
            "/user/<int:user_id>", "delete_user", self.delete_user, methods=["DELETE"]
        )

    @requires_roles("ADMIN")
    def get_all(self):
        datas = self.user_service.read_all()
        return jsonify(datas), 200

    @requires_roles("ADMIN")
    def get_one_by_id(self, user_id):
        user = self.user_service.read_one_by_id(user_id)
        return jsonify(user), 200

    @requires_roles("ADMIN")
    def save_user(self, user_id=None):
        user = self.user_service.save_user(user_id)
        return jsonify(user), 201 if not user_id else 200

    @requires_roles("ADMIN")
    def delete_user(self, user_id) -> any:
        self.user_service.delete(user_id)
        return jsonify(f"User with id: {user_id} deleted successfully"), 204
