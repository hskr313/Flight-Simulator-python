from flask import Blueprint

from JsonHelpers.FlightHelper import FlightHelper
from mappers.FlightMapper import FlightMapper
from services.FlightService import FlightService


class FlightController:
    def __init__(self,
                 flight_service: FlightService,
                 file_path
                 ):
        self.flight_service = flight_service
        self.file_path = file_path
        self.blueprint = Blueprint('flight', __name__)

