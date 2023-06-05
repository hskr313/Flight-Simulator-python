from mappers.AircraftMapper import AircraftMapper
from mappers.AirportMapper import AirportMapper
from mappers.ItineraryMapper import ItineraryMapper
from mappers.UserMapper import UserMapper
from models.Flight import Flight, Seat
from mappers.BaseMapper import BaseMapper
from models.PassengerAircraft import PassengerAircraft


class FlightMapper(BaseMapper[Flight]):

    def to_json(self, flight: Flight):
        flight_json = {
            "id": flight.id,
            "created_at": flight.created_at,
            "updated_at": flight.updated_at,
            # "stopovers": [ItineraryMapper.to_json(itinerary) for itinerary in flight.stopovers],
            "distance": flight.distance,
            "pilot": UserMapper.to_json(flight.pilot),
            "aircraft": AircraftMapper.to_json(flight.aircraft),
            "itinerary": ItineraryMapper.to_json(flight.itinerary)
        }
        if isinstance(flight.aircraft, PassengerAircraft):
            flight_json["seats"] = [SeatMapper.to_json(seat) for seat in flight.seats]
        return

    def from_json(self, flight_json: dict):
        # stopovers = [ItineraryMapper.from_json(itinerary_json) for itinerary_json in flight_json.get("stopovers", [])]
        pilot = UserMapper.from_json(flight_json.get("pilot"))
        aircraft = AircraftMapper.from_json(flight_json.get("aircraft"))
        itinerary = ItineraryMapper.from_json(flight_json.get("itinerary"))
        flight = Flight(
            # stopovers,
            flight_json.get("distance"),
            pilot,
            aircraft,
            itinerary,
        )
        flight.seats = [SeatMapper.from_json(seat) for seat in flight_json.get("seats")]
        flight.id = flight_json.get("id")
        flight.created_at = flight_json.get("created_at")
        flight.updated_at = flight_json.get("updated_at")
        return flight


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
