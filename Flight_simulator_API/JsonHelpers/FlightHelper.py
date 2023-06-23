import json
from typing import Optional, List

from JsonHelpers.BaseHelper import BaseHelper, T
from mappers.FlightMapper import FlightMapper
from models.Flight import Flight


class FlightHelper(BaseHelper[Flight]):
    """
    Helper class for operations related to Flight data storage and retrieval.
    This class extends BaseHelper and inherits all its methods.
    """

    def __init__(self, mapper: FlightMapper):
        """
        Initializes the FlightHelper with a specific FlightMapper.

        :param mapper: A FlightMapper object used for mapping between Flight objects and dictionaries.
        """
        super().__init__(mapper)
        self.file_path = 'json_files/flights.json'

    def get_all_flights_by_departure_airport(self, departure_airport):
        """
        Retrieves all flights with a specific departure airport from the flight data file.

        :param departure_airport: The departure airport to filter flights by.
        :return: A list of flight data in dictionary format, or an empty list if the file is not found.
        """
        try:
            with open(self.file_path, "r") as f:
                datas = json.load(f)

            return [data for data in datas if data["itinerary"]["departure_airport"] == departure_airport]
        except FileNotFoundError:
            return []

    def get_all_flights_by_arrival_airport(self, arrival_airport):
        """
        Retrieves all flights with a specific arrival airport from the flight data file.

        :param arrival_airport: The arrival airport to filter flights by.
        :return: A list of flight data in dictionary format, or an empty list if the file is not found.
        """
        try:
            with open(self.file_path, "r") as f:
                datas = json.load(f)

            return [data for data in datas if data["itinerary"]["arrival_airport"] == arrival_airport]
        except FileNotFoundError:
            return []
