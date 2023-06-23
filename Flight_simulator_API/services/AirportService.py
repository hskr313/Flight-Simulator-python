from flask import request

from JsonHelpers.AirportHelper import AirportHelper
from mappers.AirportMapper import AirportMapper
from models.Airport import Airport
from services.CrudService import CrudService, T, Mapper, Helper


class AirportService(CrudService[Airport, AirportMapper, AirportHelper]):

    def __init__(self, mapper: Mapper, helper: Helper, file_path):
        super().__init__(mapper, helper, file_path)

    def read_all(self):
        return super().read_all()

    def read_one_by_id(self, entity_id):
        return super().read_one_by_id(entity_id)

    def save(self, airport_id=None):
        airport_json = request.get_json()
        airport = self.mapper.from_json(airport_json)
        if airport_id:
            airport.id = airport_id
        return super().save(airport)

    def delete(self, entity_id):
        super().delete(entity_id)