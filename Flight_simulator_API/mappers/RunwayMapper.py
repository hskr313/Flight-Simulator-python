from models.Runway import Runway
from mappers.AircraftMapper import AircraftMapper
from mappers.BaseMapper import BaseMapper


class RunwayMapper(BaseMapper[Runway]):
    """
    The RunwayMapper class handles the conversion of Runway objects to JSON-compatible dictionaries and vice versa.
    """

    def to_json(self, runway: Runway):
        """
        Converts a Runway object to a dictionary that can be easily converted to JSON.

        :param runway: The Runway object to be converted.
        :return: A dictionary representing the Runway object.
        """
        return {
            "id": runway.id,
            "created_at": runway.created_at,
            "updated_at": runway.updated_at,
            "current_aircraft": runway.available
        }

    def from_json(self, runway_json: dict):
        """
        Converts a dictionary (from a JSON) to a Runway object.

        :param runway_json: The dictionary to be converted.
        :return: A Runway object.
        """
        runway = Runway()
        runway.available = runway_json.get("available")
        runway.id = runway_json.get("id")
        runway.created_at = runway_json.get("created_at")
        runway.updated_at = runway_json.get("updated_at")
        return runway
