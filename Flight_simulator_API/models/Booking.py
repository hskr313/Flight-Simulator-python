from models.BaseModel import BaseModel
from utils.GenerateConstructors import generate_constructors


@generate_constructors
class Booking(BaseModel):

    def __init__(self, date_of_booking, seat_number, user, flight):
        super().__init__()
        self.date_of_booking = date_of_booking
        self.seat_number = seat_number
        self.user = user
        self.flight = flight

