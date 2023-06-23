from flask import Blueprint, jsonify

from mappers.ItineraryMapper import ItineraryMapper
from services.ItineraryService import ItineraryService
from utils.RequestRole import requires_roles


class ItineraryController:
    def __init__(self, itinerary_service: ItineraryService):
        self.itinerary_service = itinerary_service
        self.itinerary_mapper = ItineraryMapper()
        self.blueprint = Blueprint('itineraries', __name__)
        self.blueprint.add_url_rule('/itineraries', 'get_all', self.get_all_action, methods=['GET'])
        self.blueprint.add_url_rule('/itineraries/<int:itinerary_id>', 'get_one_by_id', self.get_one_by_id_action,
                                    methods=['GET'])
        self.blueprint.add_url_rule('/itineraries', 'save_aircraft', self.save_itinerary_action, methods=['POST'])
        self.blueprint.add_url_rule('/itineraries', 'delete_aircraft', self.delete_action, methods=['DELETE'])

    @requires_roles('ADMIN')
    def get_all_action(self):
        itineraries = self.itinerary_service.read_all()
        return jsonify(itineraries), 200

    @requires_roles('ADMIN')
    def get_one_by_id_action(self, itinerary_id):
        itinerary = self.itinerary_service.read_one_by_id(itinerary_id)
        return jsonify(itinerary), 200

    @requires_roles('ADMIN')
    def save_itinerary_action(self, itinerary_id=None):
        saved_itinerary = self.itinerary_service.save(itinerary_id)
        saved_itinerary = self.itinerary_mapper.to_json(saved_itinerary)
        return jsonify(saved_itinerary), 201 if not itinerary_id else 200

    @requires_roles('ADMIN')
    def delete_action(self, itinerary_id):
        self.itinerary_service.delete(itinerary_id)
        return jsonify(''), 204
