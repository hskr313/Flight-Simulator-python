from mappers.ItineraryMapper import ItineraryMapper
from models.Airport import Airport
from mappers.BaseMapper import BaseMapper


class AirportMapper(BaseMapper[Airport]):

    def to_json(self, airport: Airport):
        return {
            "id": airport.id,
            "created_at": airport.created_at,
            "updated_at": airport.updated_at,
            "name": airport.name,
            "address": airport.address,
            "runways": airport.runways,
            "itineraries": [ItineraryMapper.to_json(itinerary) for itinerary in airport.itineraries]
        }

    def from_json(self, airport_json: dict):
        itineraries = [ItineraryMapper.from_json(itinerary) for itinerary in airport_json.get("itineraries")]
        airport = Airport(
            airport_json.get("name"),
            airport_json.get("address"),
            airport_json.get("runways"),
            itineraries
        )
        airport.id = airport_json.get("id")
        airport.created_at = airport_json.get("created_at")
        airport.updated_at = airport_json.get("updated_at")
        return airport

