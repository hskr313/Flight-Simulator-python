from models.Runway import Runway
from mappers.AircraftMapper import AircraftMapper
from mappers.BaseMapper import BaseMapper


class RunwayMapper(BaseMapper[Runway]):

    @staticmethod
    def to_json(runway: Runway):
        return {
            "id": runway.id,
            "created_at": runway.created_at,
            "updated_at": runway.updated_at,
            "current_aircraft": AircraftMapper.to_json(runway.current_aircraft)
        }

    @staticmethod
    def from_json(runway_json: dict):
        runway = Runway(AircraftMapper.from_json(runway_json.get("current_aircraft")))
        runway.id = runway_json.get("id")
        runway.created_at = runway_json.get("created_at")
        runway.updated_at = runway_json.get("updated_at")
        return runway
