from models.Runway import Runway
from mappers.AircraftMapper import AircraftMapper
from mappers.BaseMapper import BaseMapper


class RunwayMapper(BaseMapper[Runway]):
    def to_json(self, runway: Runway):
        return {
            "id": runway.id,
            "created_at": runway.created_at,
            "updated_at": runway.updated_at,
            "current_aircraft": runway.available,
        }

    def from_json(self, runway_json: dict):
        runway = Runway()
        runway.available = runway_json.get("available")
        runway.id = runway_json.get("id")
        runway.created_at = runway_json.get("created_at")
        runway.updated_at = runway_json.get("updated_at")
        return runway
