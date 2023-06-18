import json
from typing import Optional, List

from JsonHelpers.BaseHelper import BaseHelper, T
from mappers.FlightMapper import FlightMapper
from models.Flight import Flight


class FlightHelper(BaseHelper[Flight]):
    def __init__(self, mapper: FlightMapper):
        super().__init__(mapper)
        self.file_path = "json_files/flights.json"

    def get_all_flights_by_departure_airport(self, departure_airport):
        try:
            with open(self.file_path, "r") as f:
                datas = json.load(f)

            return [
                data
                for data in datas
                if data["itinerary"]["departure_airport"] == departure_airport
            ]
        except FileNotFoundError:
            return []

    def get_all_flights_by_arrival_airport(self, arrival_airport):
        try:
            with open(self.file_path, "r") as f:
                datas = json.load(f)

            return [
                data
                for data in datas
                if data["itinerary"]["arrival_airport"] == arrival_airport
            ]
        except FileNotFoundError:
            return []
