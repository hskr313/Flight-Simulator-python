from flask import Blueprint, jsonify

from services.BookingService import BookingService
from utils.RequestRole import requires_roles


class BookingController:
    def __init__(self, booking_service: BookingService):
        self.booking_service = booking_service
        self.blueprint = Blueprint("booking", __name__)
        self.blueprint.add_url_rule(
            "/bookings", "get_all", self.get_all, methods=["GET"]
        )
        self.blueprint.add_url_rule(
            "/booking/<int:booking_id>",
            "get_one_by_id",
            self.get_one_by_id,
            methods=["GET"],
        )
        self.blueprint.add_url_rule(
            "/bookings",
            "add_passenger_booking",
            self.save_passenger_booking,
            methods=["POST"],
        )

    @requires_roles("ADMIN")
    def get_all(self):
        bookings = self.booking_service.read_all()
        return jsonify(bookings), 200

    def get_one_by_id(self, booking_id):
        booking_json = self.booking_service.read_one_by_id(booking_id)
        return jsonify(booking_json), 200

    def save_passenger_booking(self, booking_id=None):
        booking = self.booking_service.save_passenger_booking(booking_id)
        return jsonify(booking), 201 if not booking_id else 200

    @requires_roles("ADMIN")
    def save_cargo_booking(self, booking_id=None):
        booking = self.booking_service.save_cargo_booking(booking_id)
        return jsonify(booking), 201 if not booking_id else 200

    @requires_roles("ADMIN")
    def delete_booking(self, booking_id):
        self.booking_service.delete(booking_id)
        return jsonify(""), 204
