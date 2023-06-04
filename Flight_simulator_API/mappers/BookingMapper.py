import datetime

from mappers.FlightMapper import FlightMapper
from mappers.UserMapper import UserMapper
from models.Booking import Booking
from mappers.BaseMapper import BaseMapper


class BookingMapper(BaseMapper[Booking]):

    @staticmethod
    def to_json(booking: Booking):
        return {
            "id": booking.id,
            "created_at": booking.created_at,
            "updated_at": booking.updated_at,
            "date_of_booking": booking.date_of_booking,
            "seat_number": booking.seat_number,
            "user": UserMapper.to_json(booking.user),
            "flight": FlightMapper.to_json(booking.flight)
        }

    @staticmethod
    def from_json(booking_json: dict):
        user = UserMapper.from_json(booking_json["user"])
        flight = FlightMapper.from_json(booking_json["flight"])
        booking = Booking(
            booking_json.get("date_of_booking"),
            booking_json.get("seat_number"),
            user,
            flight
        )
        booking.id = booking_json.get("id")
        booking.created_at = booking_json.get("created_at")
        booking.updated_at = booking_json.get("updated_at")
        return booking

    @staticmethod
    def form_to_entity():
        booking = Booking()
        booking.date_of_booking = datetime.datetime.now()
        return booking
