import datetime

from mappers.FlightMapper import FlightMapper
from mappers.UserMapper import UserMapper
from models.Booking import Booking
from mappers.BaseMapper import BaseMapper


class BookingMapper(BaseMapper[Booking]):
    """
    The BookingMapper class handles the conversion of Booking objects to JSON-compatible dictionaries and vice versa.

    It makes use of the UserMapper and FlightMapper to properly handle the conversion of associated User and Flight
    objects within a Booking.
    """

    user_mapper = UserMapper()
    flight_mapper = FlightMapper()

    def to_json(self, booking: Booking):
        """
        Converts a Booking object to a dictionary that can be easily converted to JSON.

        :param booking: The Booking object to be converted.
        :return: A dictionary representing the Booking object.
        """
        return {
            "id": booking.id,
            # "created_at": booking.created_at,
            # "updated_at": booking.updated_at,
            # "date_of_booking": booking.date_of_booking.isoformat(),
            "seat_number": booking.seat_number,
            "user": self.user_mapper.to_json(booking.user),
            "flight": self.flight_mapper.to_json(booking.flight)
        }

    def from_json(self, booking_json: dict):
        """
        Converts a dictionary (from a JSON) to a Booking object.

        :param booking_json: The dictionary to be converted.
        :return: A Booking object.
        """
        user = self.user_mapper.from_json(booking_json["user"])
        flight = self.flight_mapper.from_json(booking_json["flight"])
        booking = Booking(
            # booking_json.get("date_of_booking"),
            booking_json.get("seat_number"),
            user,
            flight
        )
        booking.id = booking_json.get("id")
        # booking.created_at = booking_json.get("created_at")
        # booking.updated_at = booking_json.get("updated_at")
        return booking

    def form_to_entity(self):
        """
        Creates and returns a new Booking object with the current date set as the date_of_booking.

        :return: A new Booking object.
        """
        booking = Booking()
        # booking.date_of_booking = datetime.datetime.now()
        return booking
