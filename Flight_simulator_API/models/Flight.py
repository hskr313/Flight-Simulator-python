from models.BaseModel import BaseModel

from models.PassengerAircraft import PassengerAircraft
from utils.GenerateConstructors import multi_constructor


class Seat:
    def __init__(self, seat_number, seat_class):
        self.seat_number = seat_number
        self.seat_class = seat_class
        self.occupied = False


@multi_constructor
class Flight(BaseModel):

    def __init__(self, distance, pilot, aircraft, itinerary):
        super().__init__()
        # self.stopovers = stopovers
        self.distance = distance
        self.pilot = pilot
        self.aircraft = aircraft
        self.itinerary = itinerary
        if isinstance(aircraft, PassengerAircraft):
            self.seats = [Seat(i + 1, 'business') for i in range(aircraft.business_capacity)] + \
                         [Seat(i + 1 + aircraft.business_capacity, 'economy') for i in range(aircraft.economy_capacity)]

    #   TODO faire un search poour avoir les vols par aeroport départ et arrivé
    #   TODO faire un mapper pour les seats aussi
