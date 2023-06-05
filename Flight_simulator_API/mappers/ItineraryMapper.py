from models.Itinerary import Itinerary
from mappers.AirportMapper import AirportMapper
from mappers.BaseMapper import BaseMapper


class ItineraryMapper(BaseMapper[Itinerary]):

    def to_json(self, itinerary: Itinerary):
        return {
            "id": itinerary.id,
            "created_at": itinerary.created_at,
            "updated_at": itinerary.updated_at,
            "departure_time": itinerary.departure_time,
            "arrival_time": itinerary.arrival_time,
            "departure_airport": AirportMapper.to_json(itinerary.departure_airport),
            "arrival_airport": AirportMapper.to_json(itinerary.arrival_airport),
            "distance": itinerary.distance
        }

    def from_json(self, itinerary_json: dict):
        itinerary = Itinerary(
            itinerary_json.get("departure_time"),
            itinerary_json.get("arrival_time"),
            AirportMapper.from_json(itinerary_json.get("departure_airport")),
            AirportMapper.from_json(itinerary_json.get("arrival_airport")),
            itinerary_json.get("distance")
        )
        itinerary.id = itinerary_json.get("id")
        itinerary.created_at = itinerary_json.get("created_at")
        itinerary.updated_at = itinerary_json.get("updated_at")
        return itinerary
