from datetime import datetime
from typing import Optional, List

from flask import request
from geopy import Nominatim
from geopy.distance import geodesic

from JsonHelpers.AircraftHelper import AircraftHelper
from JsonHelpers.FlightHelper import FlightHelper
from JsonHelpers.ItineraryHelper import ItineraryHelper
from JsonHelpers.UserHelper import UserHelper
from mappers.AircraftMapper import AircraftMapper
from mappers.FlightMapper import FlightMapper
from mappers.ItineraryMapper import ItineraryMapper
from mappers.UserMapper import UserMapper
from models.Flight import Seat, Flight
from models.Itinerary import Itinerary
from services.CrudService import CrudService, Mapper, Helper, T


class FlightService(CrudService[Flight, FlightMapper, FlightHelper]):
    """
    A service class for managing flights.

    Args:
        mapper (Mapper): The mapper for mapping flight objects.
        helper (Helper): The helper for performing CRUD operations on flights.
        file_path (str): The file path for storing flight data.

    Attributes:
        itinerary_mapper (ItineraryMapper): The mapper for mapping itinerary objects.
        itinerary_helper (ItineraryHelper): The helper for performing operations on itinerary data.
    """

    def __init__(self, mapper: Mapper, helper: Helper, file_path):
        super().__init__(mapper, helper, file_path)
        self.itinerary_mapper = ItineraryMapper()
        self.itinerary_helper = ItineraryHelper(self.itinerary_mapper)
        self.user_mapper = UserMapper()
        self.user_helper = UserHelper(self.user_mapper)
        self.aircraft_mapper = AircraftMapper()
        self.aircraft_helper = AircraftHelper(self.aircraft_mapper)

    def save_flight(self, flight_id=None) -> Flight:
        """
        Saves a flight.

        Args:
            flight_id (str, optional): The ID of the flight. Defaults to None.

        Returns:
            dict: The JSON representation of the saved flight.
        """
        flight_json = request.get_json()

        pilot_id = flight_json.get("pilot_id")
        pilot = self.user_helper.read_one_by_id(pilot_id, 'json_files/users.json')
        pilot = self.user_mapper.from_json(pilot)

        aircraft_id = flight_json.get("aircraft_id")
        aircraft = self.aircraft_helper.read_one_by_id(aircraft_id, 'json_files/aircrafts.json')
        aircraft = self.aircraft_mapper.from_json(aircraft)

        #   Upsert of itinerary
        itinerary_id = flight_json.get("itinerary_id")
        itinerary_json = self.itinerary_helper.read_one_by_id(itinerary_id, 'json_files/itineraries.json')
        itinerary = self.itinerary_mapper.from_json(itinerary_json)

        flight = Flight(
            pilot=pilot,
            aircraft=aircraft,
            itinerary=itinerary,
            departure_time=flight_json.get("departure_time")
        )

        if flight_id:
            flight.id = flight_id

        return self.helper.save(flight, self.file_path)

    def get_seat(self, flight, seat_number) -> Optional[Seat]:
        """
        Retrieves a specific seat on a flight by its seat number.

        Args:
            flight (Flight): The flight object.
            seat_number (int): The seat number.

        Returns:
            Seat: The seat object if found, None otherwise.
        """
        return next((seat for seat in flight.seats if seat.number == seat_number and not seat.occupied), None)

    def get_available_seats(self, flight) -> List[Seat]:
        """
        Retrieves a list of available seats on a flight.

        Args:
            flight (Flight): The flight object.

        Returns:
            list: A list of available seats.
        """

        return [seat for seat in flight.seats if not seat.occupied]

    def get_all_flights_by_departure_airport(self, departure_airport):
        """
        Retrieves all flights by departure airport.

        Args:
            departure_airport (str): The departure airport.

        Returns:
            list: A list of flights departing from the specified airport.
        """
        return self.helper.get_all_flights_by_departure_airport(departure_airport)

    def get_all_flights_by_arrival_airport(self, arrival_airport):
        """
        Retrieves all flights by arrival airport.

        Args:
            arrival_airport (str): The arrival airport.

        Returns:
            list: A list of flights arriving at the specified airport.
        """
        return self.helper.get_all_flights_by_arrival_airport(arrival_airport)

    def get_current_location(self, flight_id):
        """
        Retrieves the current location of a flight.

        Args:
            flight_id (str): The ID of the flight.

        Returns:
            dict: The current latitude, longitude, and time of the flight.
                   Returns None if the flight has not yet started or has already ended.
        """
        flight_json = self.read_one_by_id(flight_id)

        departure_time = datetime.fromisoformat(flight_json.get("departure_time"))
        arrival_time = datetime.fromisoformat(flight_json.get("arrival_time"))
        current_time = datetime.now()

        duration = (arrival_time - departure_time).total_seconds()
        elapsed_time = (current_time - departure_time).total_seconds()

        if elapsed_time < 0 or elapsed_time > duration:
            return None  # The flight has not yet started or has already ended

        traveled_distance_ratio = elapsed_time / duration

        start_latitude, start_longitude = Itinerary.get_coordinates(
            flight_json.get("itinerary").get("departure_airport"))
        end_latitude, end_longitude = Itinerary.get_coordinates(flight_json.get("itinerary").get("arrival_airport"))

        current_latitude = start_latitude + traveled_distance_ratio * (end_latitude - start_latitude)
        current_longitude = start_longitude + traveled_distance_ratio * (end_longitude - start_longitude)

        return {
            "latitude": current_latitude,
            "longitude": current_longitude,
            "current_time": current_time.isoformat()
        }
