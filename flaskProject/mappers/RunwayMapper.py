from models.Runway import Runway
from mappers.AircraftMapper import AircraftMapper


class RunwayMapper:

    @staticmethod
    def to_json(runway: Runway):
        return {
            "id": runway.id,
            "created_at": runway.created_at,
            "updated_at": runway.updated_at,
            "current_aircraft": AircraftMapper.to_json(runway.current_aircraft)
            # TODO ask if Aircraft Object or only boolean
        }

    @staticmethod
    def from_json(runway_json: dict):
        runway = Runway(AircraftMapper.from_json(runway_json["current_aircraft"]))
        runway.id = runway_json["id"]
        runway.created_at = runway_json["created_at"]
        runway.updated_at = runway_json["updated_at"]
        return runway
