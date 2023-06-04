from JsonHelpers.FlightHelper import FlightHelper
from JsonHelpers.UserHelper import UserHelper
from mappers.FlightMapper import FlightMapper
from mappers.UserMapper import UserMapper
from models.Booking import Booking
from services.FlightService import FlightService
from services.UserService import UserService


class BookingService:

    def __init__(self, flight_service: FlightService, flight_helper: FlightHelper, user_service: UserService, user_helper: UserHelper):
        self.flight_service = flight_service
        self.flight_helper = flight_helper
        self.user_helper = user_helper
        self.user_service = user_service

    def get_flight_from_booking(self, flight_id):
        flight = self.flight_helper.read_one_by_id(flight_id, "json_files/flights.json")
        return FlightMapper.from_json(flight)

    def get_user_from_booking(self, user_id):
        user = self.user_helper.read_one_by_id(user_id, "json_files/users.json")
        return UserMapper.from_json(user)

    def book_seat(self, seat_number, flight):
        if seat_number < 0 or seat_number >= len(flight.seats):
            raise ValueError("Le numéro de siège est invalide")

        seat = flight.seats[seat_number-1]

        if seat.occupied:
            raise ValueError("Le siège n'est pas disponible")
        else:
            seat.occupied = True
            self.flight_helper.save(flight, "json_files/flights.json")
        return seat


