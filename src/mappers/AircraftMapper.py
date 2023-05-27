from models.Aircraft import Aircraft
from models.CargoAircraft import CargoAircraft
from models.PassengerAircraft import PassengerAircraft


class AircraftMapper:

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
                aircraft_json["model"],
                aircraft_json["status"],
                aircraft_json["company_name"],
                aircraft_json["max_speed"],
                aircraft_json["fuel_tank"],
                aircraft_json["capacity"]
            )
        elif "number_of_seats" in aircraft_json:
            aircraft = PassengerAircraft(
                aircraft_json["model"],
                aircraft_json["status"],
                aircraft_json["company_name"],
                aircraft_json["max_speed"],
                aircraft_json["fuel_tank"],
                aircraft_json["number_of_seats"]
            )
        aircraft.id = aircraft_json["id"]
        aircraft.created_at = aircraft_json["created_at"]
        aircraft.updated_at = aircraft_json["updated_at"]
        return aircraft
