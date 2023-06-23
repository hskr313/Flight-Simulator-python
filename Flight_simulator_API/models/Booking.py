from models.BaseModel import BaseModel
from utils.GenerateConstructors import multi_constructor


@multi_constructor
class Booking(BaseModel):
    """
    Booking is a class representing a booking made by a user for a specific flight.
    It extends the BaseModel class with specific attributes related to bookings.

    A booking has a 'date_of_booking' attribute that denotes the date the booking was made,
    a 'seat' attribute representing the seat booked by the user, a 'user' attribute denoting the user who made the booking,
    and a 'flight' attribute representing the flight the booking is for.
    """

    def __init__(self, seat=None, user=None, flight=None):
        """
        Initializes a new instance of the Booking class.
        :param seat: Seat booked by the user.
        :param user: User who made the booking.
        :param flight: Flight the booking is for.
        """
        super().__init__()
        # self.date_of_booking = date_of_booking
        self.seat = seat
        self.user = user
        self.flight = flight

