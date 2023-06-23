from flask import Blueprint, jsonify, request

from services.FlightService import FlightService
from utils.RequestRole import requires_roles


class FlightController:
    """
    Controller for flight-related operations. It provides methods to handle flights,
    including getting all flights, getting a flight by its ID, saving a flight, deleting a flight,
    and getting the current location of a flight.
    """

    def __init__(self, flight_service: FlightService):
        """
        Initialize the FlightController with the necessary services.

        :param flight_service: Service responsible for flight-related operations.
        """
        self.flight_service = flight_service
        self.blueprint = Blueprint('flight', __name__)
        self.blueprint.add_url_rule('/flights', "get_all_flights", self.get_all_action, methods=['GET'])
        self.blueprint.add_url_rule('/flight/<int:flight_id>', "get_flight_by_id", self.get_one_by_id_action, methods=['GET'])
        self.blueprint.add_url_rule('/flights', "add_flight", self.save_flight_action, methods=['POST'])
        self.blueprint.add_url_rule('/flight/<int:flight_id>/location', "get_flight_location", self.get_flight_location, methods=['GET'])

    @requires_roles('ADMIN')
    def get_all_action(self):
        """
        Get all flights. This method requires ADMIN role.

        :return: a JSON response with a list of all flights.
        """
        flights = self.flight_service.read_all()
        return jsonify(flights), 200

    @requires_roles('ADMIN')
    def get_one_by_id_action(self, flight_id):
        """
        Get a flight by its ID. This method requires ADMIN role.

        :param flight_id: ID of the flight to be retrieved.
        :return: a JSON response with the requested flight's data.
        """
        flight = self.flight_service.read_one_by_id(flight_id)
        return jsonify(flight), 200

    @requires_roles('ADMIN')
    def save_flight_action(self, flight_id=None):
        """
        Save a flight. This method requires ADMIN role.
        If a flight ID is provided, update the existing flight.

        :param flight_id: (optional) ID of the flight to be updated.
        :return: a JSON response with the saved flight's data.
        """
        saved_flight = self.flight_service.save_flight(flight_id)
        return jsonify(saved_flight), 201 if not flight_id else 200

    @requires_roles('ADMIN')
    def delete_action(self, flight_id):
        """
        Delete a flight. This method requires ADMIN role.

        :param flight_id: ID of the flight to be deleted.
        :return: a JSON response with an empty body and status code 204.
        """
        self.flight_service.delete(flight_id)
        return jsonify(''), 204

    def get_flight_location(self, flight_id):
        """
        Get the current location of a flight.

        :param flight_id: ID of the flight whose location is to be retrieved.
        :return: a JSON response with the flight's current location or an error message.
        """
        current_location = self.flight_service.get_current_location(flight_id)
        if current_location is None:
            return jsonify('The flight has not yet started or has already ended'), 400
        return jsonify(current_location), 200
