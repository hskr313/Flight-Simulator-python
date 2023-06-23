from typing import List

from flask import request

from JsonHelpers.AirportHelper import AirportHelper
from JsonHelpers.ItineraryHelper import ItineraryHelper
from mappers.AirportMapper import AirportMapper
from mappers.ItineraryMapper import ItineraryMapper
from models.Itinerary import Itinerary
from services.CrudService import CrudService, T, Mapper, Helper


class ItineraryService(CrudService[Itinerary, ItineraryMapper, ItineraryHelper]):

    def __init__(self, mapper: Mapper, helper: Helper, file_path):
        super().__init__(mapper, helper, file_path)
        self.airport_mapper = AirportMapper()
        self.airport_helper = AirportHelper(self.airport_mapper)

    def read_all(self) -> List[dict]:
        return super().read_all()

    def read_one_by_id(self, entity_id) -> dict:
        return super().read_one_by_id(entity_id)

    def save(self, itinerary_id=None):
        itinerary_json = request.get_json()

        departure_airport = itinerary_json.get_json("departure_airport_id")
        departure_airport = self.airport_helper.read_one_by_id(departure_airport, 'json_files/airports.json')
        departure_airport = self.airport_mapper.from_json(departure_airport)

        arrival_airport = itinerary_json.get("arrival_airport_id")
        arrival_airport = self.airport_helper.read_one_by_id(arrival_airport, 'json_files/airports.json')
        arrival_airport = self.airport_mapper.from_json(arrival_airport)

        itinerary = Itinerary(
            departure_airport,
            arrival_airport
        )

        if itinerary_id:
            itinerary.id = itinerary_id

        return super().save(itinerary)

    def delete(self, entity_id) -> None:
        super().delete(entity_id)