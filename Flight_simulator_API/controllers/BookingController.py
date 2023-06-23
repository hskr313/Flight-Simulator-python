from flask import Blueprint, jsonify

from services.BookingService import BookingService
from utils.RequestRole import requires_roles


class BookingController:
    """
    Controller for booking-related operations. It provides methods to handle bookings,
    including getting all bookings, getting a booking by its ID, saving passenger and
    cargo bookings, and deleting a booking.
    """

    def __init__(self, booking_service: BookingService):
        """
        Initialize the BookingController with the necessary services.

        :param booking_service: Service responsible for booking-related operations.
        """
        self.booking_service = booking_service
        self.blueprint = Blueprint('booking', __name__)
        self.blueprint.add_url_rule('/bookings', 'get_all', self.get_all, methods=['GET'])
        self.blueprint.add_url_rule('/booking/<int:booking_id>', 'get_one_by_id', self.get_one_by_id, methods=['GET'])
        self.blueprint.add_url_rule('/bookings', 'add_passenger_booking', self.save_passenger_booking, methods=['POST'])

    @requires_roles('ADMIN')
    def get_all(self):
        """
        Get all bookings. This method requires ADMIN role.

        :return: a JSON response with a list of all bookings.
        """
        bookings = self.booking_service.read_all()
        return jsonify(bookings), 200

    def get_one_by_id(self, booking_id):
        """
        Get a booking by its ID.

        :param booking_id: ID of the booking to be retrieved.
        :return: a JSON response with the requested booking's data.
        """
        booking_json = self.booking_service.read_one_by_id(booking_id)
        return jsonify(booking_json), 200

    def save_passenger_booking(self, booking_id=None):
        """
        Save a passenger booking. If a booking ID is provided, update the existing booking.

        :param booking_id: (optional) ID of the booking to be updated.
        :return: a JSON response with the saved booking's data.
        """
        booking = self.booking_service.save_passenger_booking(booking_id)
        return jsonify(booking), 201 if not booking_id else 200

    @requires_roles('ADMIN')
    def save_cargo_booking(self, booking_id=None):
        """
        Save a cargo booking. This method requires ADMIN role.
        If a booking ID is provided, update the existing booking.

        :param booking_id: (optional) ID of the booking to be updated.
        :return: a JSON response with the saved booking's data.
        """
        booking = self.booking_service.save_cargo_booking(booking_id)
        return jsonify(booking), 201 if not booking_id else 200

    def delete_booking(self, booking_id):
        """
        Delete a booking.

        :param booking_id: ID of the booking to be deleted.
        :return: a JSON response with an empty body and status code 204.
        """
        self.booking_service.delete(booking_id)
        return jsonify(''), 204
