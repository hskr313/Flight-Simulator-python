from mappers.AircraftMapper import AircraftMapper
from mappers.AirportMapper import AirportMapper
from mappers.ItineraryMapper import ItineraryMapper
from mappers.UserMapper import UserMapper
from models.Flight import Flight


class FlightMapper:

    @staticmethod
    def to_json(flight: Flight):
        return {
            "id": flight.id,
            "created_at": flight.created_at,
            "updated_at": flight.updated_at,
            # "stopovers": [ItineraryMapper.to_json(itinerary) for itinerary in flight.stopovers],
            "distance": flight.distance,
            "pilot": UserMapper.to_json(flight.pilot),
            "aircraft": AircraftMapper.to_json(flight.aircraft),
            "itinerary": ItineraryMapper.to_json(flight.itinerary),
            "airport": AirportMapper.to_json(flight.airport)
        }

    @staticmethod
    def from_json(flight_json: dict):
        stopovers = [ItineraryMapper.from_json(itinerary_json) for itinerary_json in flight_json["stopovers"]]
        pilot = UserMapper.from_json(flight_json["pilot"])
        aircraft = AircraftMapper.from_json(flight_json["aircraft"])
        itinerary = ItineraryMapper.from_json(flight_json["itinerary"])
        airport = AirportMapper.from_json(flight_json["airport"])
        flight = Flight(
            # stopovers,
            flight_json["distance"],
            pilot,
            aircraft,
            itinerary,
            airport
        )
        flight.id = flight_json["id"]
        flight.created_at = flight_json["created_at"]
        flight.updated_at = flight_json["updated_at"]
        return flight
