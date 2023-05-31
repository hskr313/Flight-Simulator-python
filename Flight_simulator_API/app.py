from flask import Flask

from JsonHelpers.UserHelper import UserHelper
from controllers.AuthController import AuthController
from controllers.UserController import UserController
from mappers.UserMapper import UserMapper
from services.AuthService import AuthService
from services.UserService import UserService

app = Flask(__name__)

user_file_path = "json_files/users.json"
user_mapper = UserMapper()
user_helper = UserHelper(user_mapper)
user_controller = UserController(user_mapper, user_helper, user_file_path)
app.register_blueprint(user_controller.blueprint)

user_service = UserService(user_mapper, user_helper, user_file_path)
auth_service = AuthService()
auth_controller = AuthController(user_service, auth_service, user_helper, user_mapper, user_file_path)
app.register_blueprint(auth_controller.blueprint)

if __name__ == '__main__':
    app.run()
