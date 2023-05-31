from flask import Blueprint, request, jsonify
from JsonHelpers.UserHelper import UserHelper
from mappers.UserMapper import UserMapper


class UserController:
    def __init__(self, user_mapper: UserMapper, user_helper: UserHelper, file_path):
        self.user_mapper = user_mapper
        self.user_helper = user_helper
        self.file_path = file_path
        self.blueprint = Blueprint('users', __name__)
        self.blueprint.add_url_rule('/users', 'get_all', self.get_all, methods=['GET'])
        self.blueprint.add_url_rule('/users/<int:user_id>', 'get_one_by_id', self.get_one_by_id, methods=['GET'])
        self.blueprint.add_url_rule('/users', 'create_user', self.save_user, methods=['POST'])
        self.blueprint.add_url_rule('/users/<int:user_id>', 'update_user', self.save_user, methods=['PUT'])
        self.blueprint.add_url_rule('/users/<int:user_id>', 'delete_user', self.delete_user, methods=['DELETE'])

    def get_all(self):
        datas = self.user_helper.read_all(self.file_path)
        return jsonify(datas), 200

    def get_one_by_id(self, user_id):
        user_json = self.user_helper.read_one_by_id(user_id, self.file_path)
        return jsonify(user_json), 200

    def save_user(self, user_id=None):
        user_json = request.get_json()
        user = self.user_mapper.from_json(user_json)
        if user_id:
            user.id = user_id
        user = self.user_helper.save(user, self.file_path)
        user_json = self.user_mapper.to_json(user)
        return jsonify(user_json), 201 if not user_id else 200

    def delete_user(self, user_id) -> any:
        self.user_helper.delete(user_id, self.file_path)
        return jsonify(f"User with id: {user_id} deleted successfully"), 204
