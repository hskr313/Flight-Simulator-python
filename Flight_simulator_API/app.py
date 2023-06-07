import datetime

from flask import Flask, jsonify

from JsonHelpers.BookingHelper import BookingHelper
from JsonHelpers.FlightHelper import FlightHelper
from JsonHelpers.UserHelper import UserHelper
from controllers.AuthController import AuthController
from controllers.BookingController import BookingController
from controllers.UserController import UserController
from mappers.AirportMapper import AirportMapper
from mappers.BookingMapper import BookingMapper
from mappers.FlightMapper import FlightMapper
from mappers.ItineraryMapper import ItineraryMapper
from mappers.UserMapper import UserMapper
from services.AuthService import AuthService
from services.BookingService import BookingService
from services.FlightService import FlightService
from services.UserService import UserService
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Instance of all mappers
user_mapper = UserMapper()
airport_mapper = AirportMapper()
itinerary_mapper = ItineraryMapper()
flight_mapper = FlightMapper()
booking_mapper = BookingMapper()
aircraft_mapper = AirportMapper()

# Injection of all users/auth dependencies
user_file_path = "json_files/users.json"

user_helper = UserHelper(user_mapper)
user_controller = UserController(user_mapper, user_helper, user_file_path)
app.register_blueprint(user_controller.blueprint)

user_service = UserService(user_mapper, user_helper, user_file_path)
auth_service = AuthService()
auth_controller = AuthController(user_service, auth_service, user_helper, user_mapper, user_file_path)
app.register_blueprint(auth_controller.blueprint)

# Injection of all bookings dependencies
flight_helper = FlightHelper(flight_mapper)
flight_service = FlightService(flight_mapper, flight_helper, 'json_files/flights.json')
booking_file_path = "json_files/bookings.json"
booking_helper = BookingHelper(booking_mapper)
booking_service = BookingService(flight_service, flight_helper, user_service, user_helper)
booking_controller = BookingController(booking_service, booking_helper, booking_mapper, booking_file_path)
app.register_blueprint(booking_controller.blueprint)


@app.route('/test', methods=['GET'])
def test():
    return jsonify(datetime.datetime.now().isoformat()), 200


if __name__ == '__main__':
    app.run()
