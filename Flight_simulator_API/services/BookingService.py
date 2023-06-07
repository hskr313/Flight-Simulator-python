from JsonHelpers.BookingHelper import BookingHelper
from JsonHelpers.FlightHelper import FlightHelper
from JsonHelpers.UserHelper import UserHelper
from mappers.BookingMapper import BookingMapper
from mappers.FlightMapper import FlightMapper
from mappers.UserMapper import UserMapper
from models.Booking import Booking
from services.CrudService import CrudService, Mapper, Helper
from services.FlightService import FlightService
from services.UserService import UserService


class BookingService(CrudService[Booking, BookingMapper, BookingHelper]):

    def __init__(
            self,
            mapper: Mapper,
            helper: Helper,
            file_path,
            flight_helper: FlightHelper,
            user_helper: UserHelper,
            flight_mapper: FlightMapper,
            user_mapper: UserMapper
    ):
        super().__init__(mapper, helper, file_path)
        self.flight_helper = flight_helper
        self.user_helper = user_helper
        self.flight_mapper = flight_mapper
        self.user_mapper = user_mapper

    def get_flight_from_booking(self, flight_id):
        flight = self.flight_helper.read_one_by_id(flight_id, "json_files/flights.json")
        return self.flight_mapper.from_json(flight)

    def get_user_from_booking(self, user_id):
        user = self.user_helper.read_one_by_id(user_id, "json_files/users.json")
        return self.user_mapper.from_json(user)

    def book_seat(self, seat_number, flight):
        if seat_number < 0 or seat_number >= len(flight.seats):
            raise ValueError("Le numéro de siège est invalide")

        seat = flight.seats[seat_number - 1]

        if seat.occupied:
            raise ValueError("Le siège n'est pas disponible")
        else:
            seat.occupied = True
            self.flight_helper.save(flight, "json_files/flights.json")
        return seat
