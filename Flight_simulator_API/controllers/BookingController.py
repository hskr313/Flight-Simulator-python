from flask import Blueprint, jsonify, request

from JsonHelpers.BookingHelper import BookingHelper
from mappers.BookingMapper import BookingMapper
from models.Booking import Booking
from services.BookingService import BookingService
from utils.RequestRole import requires_roles


class BookingController:
    def __init__(self, booking_service: BookingService,
                 booking_helper: BookingHelper,
                 booking_mapper: BookingMapper,
                 file_path
                 ):
        self.file_path = file_path
        self.booking_mapper = booking_mapper
        self.booking_helper = booking_helper
        self.booking_service = booking_service
        self.blueprint = Blueprint('booking', __name__)
        self.blueprint.add_url_rule('/bookings', 'get_all', self.get_all, methods=['GET'])

    @requires_roles('ADMIN')
    def get_all(self):
        datas = self.booking_helper.read_all(self.file_path)
        return jsonify(datas), 200

    def get_one_by_id(self, booking_id):
        booking_json = self.booking_helper.read_one_by_id(booking_id, self.file_path)
        return jsonify(booking_json), 200

    def save_passenger_booking(self, booking_id=None):
        booking_json = request.get_json()

        booking = self.booking_mapper.form_to_entity(booking_json)

        user = self.booking_service.get_user_from_booking(booking_json.get("user_id"))
        flight = self.booking_service.get_flight_from_booking(booking_json.get("flight_id"))

        booking.user = user
        booking.flight = flight

        if booking_id:
            booking.id = booking_id
        saved_booking = self.booking_helper.save(booking, self.file_path)
        booking_json = self.booking_mapper.to_json(saved_booking)
        return jsonify(booking_json), 201 if not booking_id else 200

    @requires_roles('ADMIN')
    def save_cargo_booking(self, booking_id):
        # uniquement les admin et sans FIN
        pass

    def delete_booking(self, booking_id):
        pass
