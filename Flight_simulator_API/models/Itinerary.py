from geopy import Nominatim
from geopy.distance import geodesic

from models.BaseModel import BaseModel


class Itinerary(BaseModel):

    def __init__(self, departure_airport, arrival_airport):
        super().__init__()

        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        if self.departure_airport and self.arrival_airport:
            self.distance = Itinerary.calculate_distance(self.departure_airport, self.arrival_airport)

    @staticmethod
    def get_coordinates(airport_name):
        geolocator = Nominatim(user_agent="flight_Sim_app")
        location = geolocator.geocode(airport_name)
        if location is None:
            return None
        return location.latitude, location.longitude

    @staticmethod
    def calculate_distance(depart_airport, arrival_airport):
        location_departure_airport = Itinerary.get_coordinates(depart_airport)
        location_arrival_airport = Itinerary.get_coordinates(arrival_airport)

        distance = geodesic(location_departure_airport, location_arrival_airport).kilometers
        return distance
