from mappers.AddressMapper import AddressMapper
from mappers.ItineraryMapper import ItineraryMapper
from models.Airport import Airport
from mappers.BaseMapper import BaseMapper


class AirportMapper(BaseMapper[Airport]):
    # itinerary_mapper = ItineraryMapper()
    #
    """
    This class serves as a mapper for Airport objects, providing methods to convert Airport objects to JSON,
    and JSON to Airport objects.
    """
    address_mapper = AddressMapper()

    def to_json(self, airport: Airport):
        """
        Converts an Airport object to a dictionary (JSON).

        :param airport: Airport object to be converted.
        :return: A dictionary representation of the airport.
        """
        return {
            "id": airport.id,
            "created_at": airport.created_at,
            "updated_at": airport.updated_at,
            "name": airport.name,
            "address": self.address_mapper.to_json(airport.address),
            # "runways": airport.runways,
            # "itineraries": [self.itinerary_mapper.to_json(itinerary) for itinerary in airport.itineraries]
        }

    def from_json(self, airport_json: dict):
        """
        Converts a dictionary (JSON) to an Airport object.

        :param airport_json: The dictionary representation of an airport.
        :return: An Airport object created from the dictionary.
        """
        # itineraries = [self.itinerary_mapper.from_json(itinerary) for itinerary in airport_json.get("itineraries")]
        # itineraries = [self.itinerary_mapper.from_json(itinerary) for itinerary in airport_json.get("itineraries")]
        airport = Airport(
            airport_json.get("name"),
            self.address_mapper.from_json(airport_json.get("address")),
            # airport_json.get("runways"),
            # itineraries
        )
        airport.id = airport_json.get("id")
        airport.created_at = airport_json.get("created_at")
        airport.updated_at = airport_json.get("updated_at")
        return airport
