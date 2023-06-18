from typing import Optional, List

from flask import request
from geopy import Nominatim
from geopy.distance import geodesic

from JsonHelpers.FlightHelper import FlightHelper
from JsonHelpers.ItineraryHelper import ItineraryHelper
from mappers.FlightMapper import FlightMapper
from mappers.ItineraryMapper import ItineraryMapper
from models.Flight import Seat, Flight
from services.CrudService import CrudService, Mapper, Helper, T


class FlightService(CrudService[Flight, FlightMapper, FlightHelper]):
    def __init__(self, mapper: Mapper, helper: Helper, file_path):
        super().__init__(mapper, helper, file_path)
        self.itinerary_mapper = ItineraryMapper()
        self.itinerary_helper = ItineraryHelper(self.itinerary_mapper)

    def save_flight(self, flight_id=None):
        flight_json = request.get_json()

        pilot_id = flight_json.get_json("pilot_id")
        pilot = self.helper.read_one_by_id(pilot_id, 'json_files/users.json')

        aircraft_id = flight_json.get("aircraft_id")
        aircraft = self.helper.read_one_by_id(aircraft_id, 'json_files/aircrafts.json')

        #   Upsert of itinerary
        itinerary_json = flight_json.get("itinerary")
        itinerary = self.itinerary_mapper.from_json(itinerary_json)
        try:
            saved_itinerary = self.itinerary_helper.save(itinerary, 'json_files/itineraries.json')
        except Exception:
            raise Exception("Could not save itinerary")

        flight = Flight(
            distance=flight_json.get("distance"),
            pilot=pilot,
            aircraft=aircraft,
            itinerary=saved_itinerary
        )

        if flight_id:
            flight.id = flight_id

        return self.helper.save(flight, self.file_path)

    def get_seat(self, flight, seat_number) -> Optional[Seat]:
        return next((seat for seat in flight.seats if seat.number == seat_number and not seat.occupied), None)

    def get_available_seats(self, flight) -> List[Seat]:
        return [seat for seat in flight.seats if not seat.occupied]

    def get_all_flights_by_departure_airport(self, departure_airport):
        return self.helper.get_all_flights_by_departure_airport(departure_airport)

    def get_all_flights_by_arrival_airport(self, arrival_airport):
        return self.helper.get_all_flights_by_arrival_airport(arrival_airport)

    def get_coordinates(self, airport_name):
        geolocator = Nominatim(user_agent="flight_Sim_app")
        location = geolocator.geocode(airport_name)
        if location is None:
            return None
        return location.latitude, location.longitude

    def calculate_distance(self, start_latitude, start_longitude, end_latitude, end_longitude):
        start_point = (start_latitude, start_longitude)
        end_point = (end_latitude, end_longitude)
        distance = geodesic(start_point, end_point).kilometers
        return distance

    def calculate_flight_time(self, distance, aircraftspeed):
        travel_time = distance / aircraftspeed
        return travel_time
