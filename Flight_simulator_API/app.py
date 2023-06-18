import datetime

from flask import Flask, jsonify

from JsonHelpers.AircraftHelper import AircraftHelper
from JsonHelpers.AirportHelper import AirportHelper
from JsonHelpers.BookingHelper import BookingHelper
from JsonHelpers.FlightHelper import FlightHelper
from JsonHelpers.ItineraryHelper import ItineraryHelper
from JsonHelpers.UserHelper import UserHelper
from controllers.AuthController import AuthController
from controllers.BookingController import BookingController
from controllers.FlightController import FlightController
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

#   Instance of all mappers
user_mapper = UserMapper()
airport_mapper = AirportMapper()
itinerary_mapper = ItineraryMapper()
flight_mapper = FlightMapper()
booking_mapper = BookingMapper()
aircraft_mapper = AirportMapper()

#   Instance of all helpers
user_helper = UserHelper(user_mapper)
airport_helper = AirportHelper(airport_mapper)
itinerary_helper = ItineraryHelper(itinerary_mapper)
booking_helper = BookingHelper(booking_mapper)
flight_helper = FlightHelper(flight_mapper)
aircraft_helper = AircraftHelper(aircraft_mapper)

#   Instance of all services
user_file_path = "json_files/users.json"
user_service = UserService(user_mapper, user_helper, user_file_path)
auth_service = AuthService(user_service)
flight_file_path = "json_files/flights.json"
flight_service = FlightService(flight_mapper, flight_helper, flight_file_path)
booking_file_path = "json_files/bookings.json"
booking_service = BookingService(
    booking_mapper,
    booking_helper,
    flight_helper,
    flight_mapper,
    user_helper,
    user_mapper,
    booking_file_path,
)

#   Injection of all users/auth dependencies
user_controller = UserController(user_service)
app.register_blueprint(user_controller.blueprint)
auth_controller = AuthController(user_service, auth_service, user_mapper)
app.register_blueprint(auth_controller.blueprint)

#   Injection of all bookings dependencies
booking_controller = BookingController(booking_service)
app.register_blueprint(booking_controller.blueprint)

#   Injection of all flights dependencies
flight_controller = FlightController(flight_service)
app.register_blueprint(flight_controller.blueprint)


if __name__ == "__main__":
    app.run()
