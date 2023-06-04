from typing import Optional, List

from models.Flight import Seat


class FlightService:

    def get_seat(self, flight, seat_number) -> Optional[Seat]:
        return next((seat for seat in flight.seats if seat.number == seat_number and not seat.occupied), None)

    def get_available_seats(self, flight) -> List[Seat]:
        return [seat for seat in flight.seats if not seat.occupied]
