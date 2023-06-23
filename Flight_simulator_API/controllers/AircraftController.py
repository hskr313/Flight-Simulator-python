from flask import Blueprint, jsonify

from mappers.AircraftMapper import AircraftMapper
from services.AircraftService import AircraftService
from utils.RequestRole import requires_roles


class AircraftController:
    def __init__(self, aircraft_service: AircraftService):
        self.aircraft_service = aircraft_service
        self.aircraft_mapper = AircraftMapper()
        self.blueprint = Blueprint('aircraft', __name__)
        self.blueprint.add_url_rule('/aircrafts', 'get_all', self.get_all_action, methods=['GET'])
        self.blueprint.add_url_rule('/aircrafts/<int:aircraft_id>', 'get_one_by_id', self.get_one_by_id_action, methods=['GET'])
        self.blueprint.add_url_rule('/aircrafts', 'save_aircraft', self.save_aircraft_action, methods=['POST'])
        self.blueprint.add_url_rule('/aircrafts', 'delete_aircraft', self.delete_action, methods=['DELETE'])


    @requires_roles('ADMIN')
    def get_all_action(self):
        aircrafts = self.aircraft_service.read_all()
        return jsonify(aircrafts), 200

    @requires_roles('ADMIN')
    def get_one_by_id_action(self, aircraft_id):
        aircraft = self.aircraft_service.read_one_by_id(aircraft_id)
        return jsonify(aircraft), 200

    @requires_roles('ADMIN')
    def save_aircraft_action(self, aircraft_id=None):
        saved_aircraft = self.aircraft_service.save(aircraft_id)
        saved_aircraft = self.aircraft_mapper.to_json(saved_aircraft)
        return jsonify(saved_aircraft), 201 if not aircraft_id else 200

    @requires_roles('ADMIN')
    def delete_action(self, aircraft_id):
        self.aircraft_service.delete(aircraft_id)
        return jsonify(''), 204
