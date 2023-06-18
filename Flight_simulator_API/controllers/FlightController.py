from flask import Blueprint, jsonify, request

from services.FlightService import FlightService
from utils.RequestRole import requires_roles


class FlightController:
    def __init__(self, flight_service: FlightService):
        self.flight_service = flight_service
        self.blueprint = Blueprint("flight", __name__)
        self.blueprint.add_url_rule(
            "/flights", "get_all_flights", self.get_all_action, methods=["GET"]
        )
        self.blueprint.add_url_rule(
            "/flight/<int:flight_id>",
            "get_flight_by_id",
            self.get_one_by_id_action,
            methods=["GET"],
        )
        self.blueprint.add_url_rule(
            "/flights", "add_flight", self.save_flight_action, methods=["POST"]
        )

    @requires_roles("ADMIN")
    def get_all_action(self):
        flights = self.flight_service.read_all()
        return jsonify(flights), 200

    def get_one_by_id_action(self, flight_id):
        flight = self.flight_service.read_one_by_id(flight_id)
        return jsonify(flight), 200

    @requires_roles("ADMIN")
    def save_flight_action(self, flight_id=None):
        saved_flight = self.flight_service.save_flight(flight_id)
        return jsonify(saved_flight), 201 if not flight_id else 200

    @requires_roles("ADMIN")
    def delete_action(self, flight_id):
        self.flight_service.delete(flight_id)
        return jsonify(""), 204
