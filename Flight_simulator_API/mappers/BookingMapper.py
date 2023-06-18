import datetime

from mappers.FlightMapper import FlightMapper
from mappers.UserMapper import UserMapper
from models.Booking import Booking
from mappers.BaseMapper import BaseMapper


class BookingMapper(BaseMapper[Booking]):
    user_mapper = UserMapper()
    flight_mapper = FlightMapper()

    def to_json(self, booking: Booking):
        return {
            "id": booking.id,
            "created_at": booking.created_at,
            "updated_at": booking.updated_at,
            "date_of_booking": booking.date_of_booking,
            "seat_number": booking.seat_number,
            "user": self.user_mapper.to_json(booking.user),
            "flight": self.flight_mapper.to_json(booking.flight),
        }

    def from_json(self, booking_json: dict):
        user = self.user_mapper.from_json(booking_json["user"])
        flight = self.flight_mapper.from_json(booking_json["flight"])
        booking = Booking(
            booking_json.get("date_of_booking"),
            booking_json.get("seat_number"),
            user,
            flight,
        )
        booking.id = booking_json.get("id")
        booking.created_at = booking_json.get("created_at")
        booking.updated_at = booking_json.get("updated_at")
        return booking

    def form_to_entity(self):
        booking = Booking()
        booking.date_of_booking = datetime.datetime.now()
        return booking
