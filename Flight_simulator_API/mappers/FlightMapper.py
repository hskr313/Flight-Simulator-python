from mappers.AircraftMapper import AircraftMapper
from mappers.AirportMapper import AirportMapper
from mappers.ItineraryMapper import ItineraryMapper
from mappers.UserMapper import UserMapper
from models.Flight import Flight, Seat
from mappers.BaseMapper import BaseMapper
from models.PassengerAircraft import PassengerAircraft


class SeatMapper(BaseMapper[Seat]):
    def to_json(self, seat: Seat):
        seat_json = {
            "seat_number": seat.seat_number,
            "seat_class": seat.seat_class,
            "occupied": seat.occupied
        }
        return seat_json

    def from_json(self, seat_json: dict):
        seat = Seat(
            seat_json.get("seat_class"),
            seat_json.get("seat_number")
        )
        seat.occupied = seat_json.get("occupied")
        return seat


class FlightMapper(BaseMapper[Flight]):
    user_mapper = UserMapper()
    aircraft_mapper = AircraftMapper()
    itinerary_mapper = ItineraryMapper()
    seat_mapper = SeatMapper()

    def to_json(self, flight: Flight):
        flight_json = {
            "id": flight.id,
            "created_at": flight.created_at,
            "updated_at": flight.updated_at,
            "pilot": self.user_mapper.to_json(flight.pilot),
            "aircraft": self.aircraft_mapper.to_json(flight.aircraft),
            "itinerary": self.itinerary_mapper.to_json(flight.itinerary),
            "departure_time": flight.departure_time,
            "arrival_time": flight.arrival_time,
        }
        if isinstance(flight.aircraft, PassengerAircraft):
            flight_json["seats"] = [self.seat_mapper.to_json(seat) for seat in flight.seats]
        return

    def from_json(self, flight_json: dict):
        pilot = self.user_mapper.from_json(flight_json.get("pilot"))
        aircraft = self.aircraft_mapper.from_json(flight_json.get("aircraft"))
        itinerary = self.itinerary_mapper.from_json(flight_json.get("itinerary"))
        flight = Flight(
            flight_json.get("departure_time"),
            flight_json.get("arrival_time"),
            pilot,
            aircraft,
            itinerary,
        )
        if isinstance(aircraft, PassengerAircraft):
            flight.seats = [self.seat_mapper.from_json(seat) for seat in flight_json.get("seats")]
        flight.id = flight_json.get("id")
        flight.created_at = flight_json.get("created_at")
        flight.updated_at = flight_json.get("updated_at")
        return flight
