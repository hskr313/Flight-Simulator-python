from models.Airport import Airport
from mappers.BaseMapper import BaseMapper


class AirportMapper(BaseMapper[Airport]):

    @staticmethod
    def to_json(airport: Airport):
        return {
            "id": airport.id,
            "created_at": airport.created_at,
            "updated_at": airport.updated_at,
            "name": airport.name,
            "address": airport.address,
            "runways": airport.runways,
            "itinerary": airport.itinerary
        }

    @staticmethod
    def from_json(airport_json: dict):
        airport = Airport(
            airport_json.get("name"),
            airport_json.get("address"),
            airport_json.get("runways"),
            airport_json.get("itinerary")
        )
        airport.id = airport_json.get("id")
        airport.created_at = airport_json.get("created_at")
        airport.updated_at = airport_json.get("updated_at")
        return airport

#Todo mapper les runways et itinerary to object