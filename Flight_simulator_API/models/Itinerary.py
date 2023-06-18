from models.BaseModel import BaseModel


class Itinerary(BaseModel):

    def __init__(self, departure_airport, arrival_airport, distance):
        super().__init__()

        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.distance = distance
