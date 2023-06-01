import datetime

from flask import Flask, jsonify

from JsonHelpers.BookingHelper import BookingHelper
from JsonHelpers.UserHelper import UserHelper
from controllers.AuthController import AuthController
from controllers.BookingController import BookingController
from controllers.UserController import UserController
from mappers.BookingMapper import BookingMapper
from mappers.UserMapper import UserMapper
from services.AuthService import AuthService
from services.BookingService import BookingService
from services.UserService import UserService
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Injection of all users/auth dependencies
user_file_path = "json_files/users.json"
user_mapper = UserMapper()
user_helper = UserHelper(user_mapper)
user_controller = UserController(user_mapper, user_helper, user_file_path)
app.register_blueprint(user_controller.blueprint)

user_service = UserService(user_mapper, user_helper, user_file_path)
auth_service = AuthService()
auth_controller = AuthController(user_service, auth_service, user_helper, user_mapper, user_file_path)
app.register_blueprint(auth_controller.blueprint)

# Injection of all bookings dependencies
booking_file_path = "json_files/bookings.json"
booking_mapper = BookingMapper()
booking_helper = BookingHelper(booking_mapper)
booking_service = BookingService()
booking_controller = BookingController(booking_service, booking_helper, booking_mapper, booking_file_path)
app.register_blueprint(booking_controller.blueprint)


@app.route('/test', methods=['GET'])
def test():
    return jsonify(datetime.datetime.now().isoformat()), 200


if __name__ == '__main__':
    app.run()

    #   TODO faire un decorateur qui get le user dans chaque requetes
    #    pour voir si on a le droit d'effectuer un call API OU PAS
