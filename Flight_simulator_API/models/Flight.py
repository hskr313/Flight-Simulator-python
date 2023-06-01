from models.BaseModel import BaseModel
from models.Itinerary import Itinerary
from typing import List

from models.PassengerAircraft import PassengerAircraft


class Flight(BaseModel):

    def __init__(self, distance, pilot, aircraft, itinerary, airport):
        super().__init__()
        # self.stopovers: List[Itinerary] = stopovers
        self.distance = distance
        self.pilot = pilot
        self.aircraft = aircraft
        self.itinerary = itinerary
        self.airport = airport
        if isinstance(aircraft, PassengerAircraft):
            self.seats = [True] * self.aircraft.number_of_seats  # TODO est ce que l'idée est bonne ?
