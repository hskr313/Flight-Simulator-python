from flask import Blueprint, jsonify, request

from services.FlightService import FlightService
from utils.RequestRole import requires_roles


class FlightController:
    def __init__(self,
                 flight_service: FlightService,
                 file_path
                 ):
        self.flight_service = flight_service
        self.file_path = file_path
        self.blueprint = Blueprint('flight', __name__)

    @requires_roles('ADMIN')
    def get_all_action(self):
        flights = self.flight_service.read_all()
        return jsonify(flights), 200

    @requires_roles('ADMIN')
    def get_one_by_id_action(self, flight_id):
        flight = self.flight_service.read_one_by_id(flight_id)
        return jsonify(flight), 200

    @requires_roles('ADMIN')
    def save_flight_action(self, flight_id=None):
        saved_flight = self.flight_service.save_flight(flight_id)
        return jsonify(saved_flight), 201 if not flight_id else 200
