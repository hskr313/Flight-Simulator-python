from models.Itinerary import Itinerary
from mappers.AirportMapper import AirportMapper
from mappers.BaseMapper import BaseMapper


class ItineraryMapper(BaseMapper[Itinerary]):

    @staticmethod
    def to_json(itinerary: Itinerary):
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

    @staticmethod
    def from_json(itinerary_json: dict):
        itinerary = Itinerary(
            itinerary_json["departure_time"],
            itinerary_json["arrival_time"],
            AirportMapper.from_json(itinerary_json["departure_airport"]),
            AirportMapper.from_json(itinerary_json["arrival_airport"]),
            itinerary_json["distance"]
        )
        itinerary.id = itinerary_json["id"]
        itinerary.created_at = itinerary_json["created_at"]
        itinerary.updated_at = itinerary_json["updated_at"]
        return itinerary
