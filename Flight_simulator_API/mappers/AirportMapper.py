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
            airport_json["name"],
            airport_json["address"],
            airport_json["runways"],
            airport_json["itinerary"]
        )
        airport.id = airport_json["id"]
        airport.created_at = airport_json["created_at"]
        airport.updated_at = airport_json["updated_at"]
        return airport
