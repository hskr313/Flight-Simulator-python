from services.AircraftService import AircraftService
from flask import Blueprint, jsonify, request


class AircraftController:
    def __init__(self, aircraft_service: AircraftService):
        self.aircraft_service = aircraft_service
        self.blueprint = Blueprint("aircraft", __name__)
        self.blueprint.add_url_rule("")

    def get_all_action(self):
        aircrafts = self.aircraft_service.read_all()
        return jsonify(aircrafts), 200

    def get_one_by_id_action(self, aircraft_id):
        aircraft = self.aircraft_service.read_one_by_id(aircraft_id)
        return jsonify(aircraft), 200

    def save_aircraft(self, aircraft_id):
        saved_aircraft = self.aircraft_service.save(aircraft_id)
        return jsonify(saved_aircraft), 201 if not aircraft_id else 200
