from JsonHelpers.AirportHelper import AirportHelper
from mappers.AirportMapper import AirportMapper
from models.Airport import Airport
from services.CrudService import CrudService


class AirportService(CrudService[Airport, AirportMapper, AirportHelper]):
    pass
