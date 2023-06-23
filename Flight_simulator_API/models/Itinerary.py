from geopy import Nominatim
from geopy.distance import geodesic

from models.Airport import Airport
from models.BaseModel import BaseModel


class Itinerary(BaseModel):
    """
    The Itinerary class represents a flight itinerary. It extends the BaseModel class with several additional attributes.
    Attributes:
        departure_airport: The departure airport for the itinerary.
        arrival_airport: The arrival airport for the itinerary.
        distance: The calculated distance between the departure and arrival airports.
    """

    def __init__(self, departure_airport, arrival_airport):
        """
        Initializes a new instance of the Itinerary class.
        :param departure_airport: The departure airport for the itinerary.
        :param arrival_airport: The arrival airport for the itinerary.
        """
        super().__init__()

        self.departure_airport: Airport = departure_airport
        self.arrival_airport: Airport = arrival_airport
        if self.departure_airport and self.arrival_airport:
            self.distance = Itinerary.calculate_distance(self.departure_airport.name, self.arrival_airport.name)
    @staticmethod
    def get_coordinates(airport_city_name):
        """
        Retrieves the coordinates for a given airport.
        :param airport_city_name: The name of the city where the airport is located.
        :return: The latitude and longitude of the airport.
        """
        geolocator = Nominatim(user_agent="flight_Sim_app")
        location = geolocator.geocode(airport_city_name + " Airport")
        if location is None:
            return None
        return location.latitude, location.longitude

    @staticmethod
    def calculate_distance(depart_airport, arrival_airport):
        """
        Calculates the distance between two airports.
        :param depart_airport: The departure airport.
        :param arrival_airport: The arrival airport.
        :return: The distance between the two airports in kilometers.
        """
        location_departure_airport = Itinerary.get_coordinates(depart_airport)
        location_arrival_airport = Itinerary.get_coordinates(arrival_airport)

        distance = geodesic(location_departure_airport, location_arrival_airport).kilometers
        return distance
