from flask import request

from JsonHelpers.AircraftHelper import AircraftHelper
from mappers.AircraftMapper import AircraftMapper
from models.Aircraft import Aircraft
from services.CrudService import CrudService, T, Mapper, Helper


class AircraftService(CrudService[Aircraft, AircraftMapper, AircraftHelper]):

    def __init__(self, mapper: Mapper, helper: Helper, file_path):
        super().__init__(mapper, helper, file_path)

    def read_all(self):
        return super().read_all()

    def read_one_by_id(self, entity_id):
        return super().read_one_by_id(entity_id)

    def save(self, aircraft_id):
        aircraft_json = request.get_json()
        aircraft = self.mapper.from_json(aircraft_json)

        if aircraft_id:
            aircraft.id = aircraft_id
        return super().save(aircraft)

    def delete(self, entity_id):
        super().delete(entity_id)