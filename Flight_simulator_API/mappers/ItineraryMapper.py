from models.Itinerary import Itinerary
from mappers.BaseMapper import BaseMapper


class ItineraryMapper(BaseMapper[Itinerary]):
    """
    The ItineraryMapper class handles the conversion of Itinerary objects to JSON-compatible dictionaries and vice versa.
    It makes use of the AirportMapper to properly handle the conversion of associated Airport objects within an Itinerary.
    """

    def to_json(self, itinerary: Itinerary):
        """
        Converts an Itinerary object to a dictionary that can be easily converted to JSON.

        :param itinerary: The Itinerary object to be converted.
        :return: A dictionary representing the Itinerary object.
        """
        from mappers.AirportMapper import AirportMapper
        airport_mapper = AirportMapper()
        return {
            "id": itinerary.id,
            "created_at": itinerary.created_at,
            "updated_at": itinerary.updated_at,
            "departure_airport": airport_mapper.to_json(itinerary.departure_airport),
            "arrival_airport": airport_mapper.to_json(itinerary.arrival_airport),
            "distance": itinerary.distance
        }

    def from_json(self, itinerary_json: dict):
        """
        Converts a dictionary (from a JSON) to an Itinerary object.

        :param itinerary_json: The dictionary to be converted.
        :return: An Itinerary object.
        """
        from mappers.AirportMapper import AirportMapper
        airport_mapper = AirportMapper()
        itinerary = Itinerary(
            airport_mapper.from_json(itinerary_json.get("departure_airport")),
            airport_mapper.from_json(itinerary_json.get("arrival_airport")),
        )
        itinerary.id = itinerary_json.get("id")
        itinerary.created_at = itinerary_json.get("created_at")
        itinerary.updated_at = itinerary_json.get("updated_at")
        itinerary.distance = itinerary_json.get("distance")
        return itinerary
