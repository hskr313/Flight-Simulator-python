from models.BaseModel import BaseModel
from models.PassengerAircraft import PassengerAircraft
from utils.GenerateConstructors import multi_constructor


class Seat:
    """
    The Seat class represents a seat in an aircraft.
    Attributes:
        seat_number: An identifier for the seat.
        seat_class: The class of the seat (e.g., 'business', 'economy').
        occupied: A boolean indicating whether the seat is occupied.
    """
    def __init__(self, seat_number, seat_class):
        """
        Initializes a new instance of the Seat class.
        :param seat_number: The number of the seat.
        :param seat_class: The class of the seat.
        """
        self.seat_number = seat_number
        self.seat_class = seat_class
        self.occupied = False


@multi_constructor
class Flight(BaseModel):
    """
    The Flight class represents a flight. It extends the BaseModel class with several additional attributes.
    Attributes:
        pilot: The pilot of the flight.
        aircraft: The aircraft used for the flight.
        itinerary: The itinerary of the flight.
        departure_time: The departure time of the flight.
        arrival_time: The arrival time of the flight.
        seats: A list of seats in the aircraft (only present if the aircraft is a PassengerAircraft).
    """
    def __init__(self, pilot, aircraft, itinerary, departure_time):
        """
        Initializes a new instance of the Flight class.
        :param pilot: The pilot of the flight.
        :param aircraft: The aircraft used for the flight.
        :param itinerary: The itinerary of the flight.
        :param departure_time: The departure time of the flight.
        """
        super().__init__()
        self.pilot = pilot
        self.aircraft = aircraft
        self.itinerary = itinerary
        self.departure_time = departure_time
        self.arrival_time = departure_time + self.calculate_flight_time(self.itinerary.distance, self.aircraft.max_speed)
        if isinstance(aircraft, PassengerAircraft):
            self.seats = [Seat(i + 1, 'business') for i in range(aircraft.business_capacity)] + \
                         [Seat(i + 1 + aircraft.business_capacity, 'economy') for i in range(aircraft.economy_capacity)]

    #   TODO faire un search poour avoir les vols par aeroport départ et arrivé
    #   TODO faire un mapper pour les seats aussi

    def calculate_flight_time(self, distance, aircraftspeed):
        """
        Calculate the time of flight based on distance and aircraft speed.
        :param distance: The distance of the flight.
        :param aircraftspeed: The speed of the aircraft.
        :return: The flight time.
        """
        travel_time = distance / aircraftspeed
        return travel_time
