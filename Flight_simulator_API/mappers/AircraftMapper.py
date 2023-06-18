from models.Aircraft import Aircraft
from models.CargoAircraft import CargoAircraft
from models.PassengerAircraft import PassengerAircraft
from mappers.BaseMapper import BaseMapper, T


class AircraftMapper(BaseMapper[Aircraft]):
    def to_json(self, aircraft: Aircraft):
        aircraft_json = {
            "id": aircraft.id,
            "created_at": aircraft.created_at,
            "updated_at": aircraft.updated_at,
            "model": aircraft.model,
            "available": aircraft.available,
            "company_name": aircraft.company_name,
            "max_speed": aircraft.max_speed,
            "fuel_tank": aircraft.fuel_tank,
        }

        if isinstance(aircraft, CargoAircraft):
            aircraft_json["capacity"] = aircraft.capacity
        elif isinstance(aircraft, PassengerAircraft):
            aircraft_json["business_capacity"] = aircraft.business_capacity
            aircraft_json["economy_capacity"] = aircraft.economy_capacity

        return aircraft_json

    def from_json(self, aircraft_json: dict):
        if "capacity" in aircraft_json:
            aircraft = CargoAircraft(
                aircraft_json.get("model"),
                aircraft_json.get("company_name"),
                aircraft_json.get("max_speed"),
                aircraft_json.get("fuel_tank"),
                aircraft_json.get("capacity"),
            )
        else:
            aircraft = PassengerAircraft(
                aircraft_json.get("model"),
                aircraft_json.get("company_name"),
                aircraft_json.get("max_speed"),
                aircraft_json.get("fuel_tank"),
                aircraft_json.get("business_capacity"),
                aircraft_json.get("economy_capacity"),
            )
        aircraft.id = aircraft_json.get("id")
        aircraft.available = aircraft_json.get("available")
        aircraft.created_at = aircraft_json.get("created_at")
        aircraft.updated_at = aircraft_json.get("updated_at")
        return aircraft
