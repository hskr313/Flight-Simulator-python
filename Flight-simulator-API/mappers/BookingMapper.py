from mappers.FlightMapper import FlightMapper
from mappers.UserMapper import UserMapper
from models.Booking import Booking


class BookingMapper:

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
            booking_json["date_of_booking"],
            booking_json["seat_number"],
            user,
            flight
        )
        booking.id = booking_json["id"]
        booking.created_at = booking_json["created_at"]
        booking.updated_at = booking_json["updated_at"]
        return booking
