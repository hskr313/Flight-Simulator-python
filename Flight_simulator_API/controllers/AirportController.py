
from flask import Blueprint, jsonify, request

from mappers.AirportMapper import AirportMapper
from services.AirportService import AirportService
from utils.RequestRole import requires_roles


class AirportController:
    def __init__(self, airport_service: AirportService):
        self.airport_service = airport_service
        self.airport_mapper = AirportMapper()
        self.blueprint = Blueprint('airport', __name__)
        self.blueprint.add_url_rule('/airports', 'get_all', self.get_all_action, methods=['GET'])
        self.blueprint.add_url_rule('/airports/<int:airport_id>', 'get_one_by_id', self.get_one_by_id_action,
                                    methods=['GET'])
        self.blueprint.add_url_rule('/airports', 'save_aircraft', self.save_airport_action, methods=['POST'])
        self.blueprint.add_url_rule('/airports', 'delete_aircraft', self.delete_action, methods=['DELETE'])

    @requires_roles('ADMIN')
    def get_all_action(self):
        airports = self.airport_service.read_all()
        return jsonify(airports), 200

    @requires_roles('ADMIN')
    def get_one_by_id_action(self, airport_id):
        airport = self.airport_service.read_one_by_id(airport_id)
        return jsonify(airport), 200

    @requires_roles('ADMIN')
    def save_airport_action(self, airport_id=None):
        saved_airport = self.airport_service.save(airport_id)
        saved_airport = self.airport_mapper.to_json(saved_airport)
        return jsonify(saved_airport), 201 if not airport_id else 200

    @requires_roles('ADMIN')
    def delete_action(self, airport_id):
        self.airport_service.delete(airport_id)
        return jsonify(''), 204
