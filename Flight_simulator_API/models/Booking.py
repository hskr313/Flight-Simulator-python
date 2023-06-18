from models.BaseModel import BaseModel
from utils.GenerateConstructors import multi_constructor


@multi_constructor
class Booking(BaseModel):
    def __init__(self, date_of_booking=None, seat=None, user=None, flight=None):
        super().__init__()
        self.date_of_booking = date_of_booking
        self.seat = seat
        self.user = user
        self.flight = flight

    #   TODO faire le choix des places dans une reservation

    #   TODO faire le moyen de paiements suivant le calcul d'itineraires

    #   TODO iplementer les services de booking
