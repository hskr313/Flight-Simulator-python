from flask import request

from JsonHelpers.BookingHelper import BookingHelper
from JsonHelpers.FlightHelper import FlightHelper
from JsonHelpers.UserHelper import UserHelper
from mappers.BookingMapper import BookingMapper
from mappers.FlightMapper import FlightMapper
from mappers.UserMapper import UserMapper
from models.Booking import Booking
from services.CrudService import CrudService, Mapper, Helper


class BookingService(CrudService[Booking, BookingMapper, BookingHelper]):

    def __init__(
            self,
            mapper: Mapper,
            helper: Helper,
            flight_helper: FlightHelper,
            flight_mapper: FlightMapper,
            user_helper: UserHelper,
            user_mapper: UserMapper,
            file_path
    ):
        super().__init__(mapper, helper, file_path)
        self.flight_helper = flight_helper
        self.user_helper = user_helper
        self.flight_mapper = flight_mapper
        self.user_mapper = user_mapper

    def save_passenger_booking(self, booking_id=None):
        booking_json = request.get_json()

        booking = self.mapper.form_to_entity()

        user = self.get_user_from_booking(booking_json.get("user_id"))
        flight = self.get_flight_from_booking(booking_json.get("flight_id"))
        booking_seat = self.book_seat(booking_json.get("seat_number"), flight)

        booking.user = user
        booking.flight = flight
        booking.seat = booking_seat

        if booking_id:
            booking.id = booking_id
        saved_booking = self.helper.save(booking, self.file_path)
        booking_json = self.mapper.to_json(saved_booking)
        return booking_json

    def save_cargo_booking(self, booking_id):
        booking_json = request.get_json()

        booking = self.mapper.form_to_entity()

        user = self.get_user_from_booking(booking_json.get("user_id"))
        flight = self.get_flight_from_booking(booking_json.get("flight_id"))

        booking.user = user
        booking.flight = flight

        if booking_id:
            booking.id = booking_id
        saved_booking = self.helper.save(booking, self.file_path)
        booking_json = self.mapper.to_json(saved_booking)
        return booking_json

    def get_flight_from_booking(self, flight_id):
        flight = self.flight_helper.read_one_by_id(flight_id, "json_files/flights.json")
        return self.flight_mapper.from_json(flight)

    def get_user_from_booking(self, user_id):
        user = self.user_helper.read_one_by_id(user_id, "json_files/users.json")
        return self.user_mapper.from_json(user)

    def book_seat(self, seat_number, flight):
        if seat_number < 0 or seat_number >= len(flight.seats):
            raise ValueError("Seat number is incorrect")

        seat = flight.seats[seat_number - 1]

        if seat.occupied:
            raise ValueError("Seat number is unavailable")
        else:
            seat.occupied = True
            self.flight_helper.save(flight, "json_files/flights.json")
        return seat
