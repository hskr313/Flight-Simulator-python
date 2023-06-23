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
    """
    A service class for managing bookings.

    Args:
        mapper (Mapper): The mapper for mapping booking objects.
        helper (Helper): The helper for performing CRUD operations on bookings.
        flight_helper (FlightHelper): The helper for performing operations on flight data.
        flight_mapper (FlightMapper): The mapper for mapping flight objects.
        user_helper (UserHelper): The helper for performing operations on user data.
        user_mapper (UserMapper): The mapper for mapping user objects.
        file_path (str): The file path for storing booking data.

    Attributes:
        flight_helper (FlightHelper): The helper for performing operations on flight data.
        user_helper (UserHelper): The helper for performing operations on user data.
        flight_mapper (FlightMapper): The mapper for mapping flight objects.
        user_mapper (UserMapper): The mapper for mapping user objects.
    """

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
        """
        Saves a passenger booking.

        Args:
            booking_id (str, optional): The ID of the booking. Defaults to None.

        Returns:
            dict: The JSON representation of the saved booking.
        """
        booking_json = request.get_json()

        booking = self.mapper.form_to_entity()

        user = self.user_helper.read_one_by_id(booking_json.get("user_id"), 'json_files/users.json')
        user = self.user_mapper.from_json(user)

        flight = self.flight_helper.read_one_by_id(booking_json.get("flight_id"), 'json_files/flights.json')
        flight = self.flight_mapper.from_json(flight)

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
        """
        Saves a cargo booking.

        Args:
            booking_id (str): The ID of the booking.

        Returns:
            dict: The JSON representation of the saved booking.
        """
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
        """
        Retrieves a flight object based on the flight ID.

        Args:
            flight_id (str): The ID of the flight.

        Returns:
            Flight: The flight object.
        """
        flight = self.flight_helper.read_one_by_id(flight_id, "json_files/flights.json")
        return self.flight_mapper.from_json(flight)

    def get_user_from_booking(self, user_id):
        """
        Retrieves a user object based on the user ID.

        Args:
            user_id (str): The ID of the user.

        Returns:
            User: The user object.
        """
        user = self.user_helper.read_one_by_id(user_id, "json_files/users.json")
        return self.user_mapper.from_json(user)

    def book_seat(self, seat_number, flight):
        """
        Books a seat on a flight.

        Args:
            seat_number (int): The seat number.
            flight (Flight): The flight object.

        Returns:
            Seat: The booked seat.

        Raises:
            ValueError: If the seat number is incorrect or unavailable.
        """
        if seat_number < 0 or seat_number >= len(flight.seats):
            raise ValueError("Seat number is incorrect")

        seat = flight.seats[seat_number - 1]

        if seat.occupied:
            raise ValueError("Seat number is unavailable")
        else:
            seat.occupied = True
            self.flight_helper.save(flight, "json_files/flights.json")
        return seat
