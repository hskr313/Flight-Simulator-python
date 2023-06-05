from typing import Optional, List

from flask import request

from JsonHelpers.BaseHelper import BaseHelper
from JsonHelpers.FlightHelper import FlightHelper
from mappers.BaseMapper import BaseMapper
from mappers.FlightMapper import FlightMapper
from models.Flight import Seat, Flight
from services.CrudService import CrudService, Mapper, Helper, T


class FlightService(CrudService[Flight, FlightMapper, FlightHelper]):
    def __init__(self, mapper: Mapper, helper: Helper, file_path):
        super().__init__(mapper, helper, file_path)

    def save_flight(self, flight_id=None):
        flight_json = request.get_json()

        pilot_id = flight_json.get_json("pilot_id")
        pilot = self.helper.read_one_by_id(pilot_id, 'json_files/users.json')

        aircraft_id = flight_json.get("aircraft_id")
        aircraft = self.helper.read_one_by_id(aircraft_id, 'json_files/aircrafts.json')

        #   TODO faire un upsert pour l'itineraire
        itinerary_id = flight_json.get("itinerary_id")
        itinerary = self.helper.read_one_by_id(itinerary_id, 'json_files/itineraries.json')

        flight = Flight(distance=flight_json.get("distance"),
                        pilot=pilot,
                        aircraft=aircraft,
                        itinerary=itinerary
                        )

        if flight_id:
            flight.id = flight_id

        return self.helper.save(flight, self.file_path)

    def get_seat(self, flight, seat_number) -> Optional[Seat]:
        return next((seat for seat in flight.seats if seat.number == seat_number and not seat.occupied), None)

    def get_available_seats(self, flight) -> List[Seat]:
        return [seat for seat in flight.seats if not seat.occupied]
