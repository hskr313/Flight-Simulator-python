from models.Aircraft import Aircraft
from models.CargoAircraft import CargoAircraft
from models.PassengerAircraft import PassengerAircraft
from mappers.BaseMapper import BaseMapper, T


class AircraftMapper(BaseMapper[Aircraft]):

    @staticmethod
    def to_json(aircraft: Aircraft):
        aircraft_json = {
            "id": aircraft.id,
            "created_at": aircraft.created_at,
            "updated_at": aircraft.updated_at,
            "model": aircraft.model,
            "status": aircraft.status,
            "company_name": aircraft.company_name,
            "max_speed": aircraft.max_speed,
            "fuel_tank": aircraft.fuel_tank
        }

        if isinstance(aircraft, CargoAircraft):
            aircraft_json["capacity"] = aircraft.capacity
        elif isinstance(aircraft, PassengerAircraft):
            aircraft_json["number_of_seats"] = aircraft.number_of_seats

        return aircraft_json

    @staticmethod
    def from_json(aircraft_json: dict):
        if "capacity" in aircraft_json:
            aircraft = CargoAircraft(
                aircraft_json.get("model"),
                aircraft_json.get("status"),
                aircraft_json.get("company_name"),
                aircraft_json.get("max_speed"),
                aircraft_json.get("fuel_tank"),
                aircraft_json.get("capacity")
            )
        elif "number_of_seats" in aircraft_json:
            aircraft = PassengerAircraft(
                aircraft_json.get("model"),
                aircraft_json.get("status"),
                aircraft_json.get("company_name"),
                aircraft_json.get("max_speed"),
                aircraft_json.get("fuel_tank"),
                aircraft_json.get("number_of_seats")
            )
        aircraft.id = aircraft_json.get("id")
        aircraft.created_at = aircraft_json.get("created_at")
        aircraft.updated_at = aircraft_json.get("updated_at")
        return aircraft
