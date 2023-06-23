from JsonHelpers.AircraftHelper import AircraftHelper
from mappers.AircraftMapper import AircraftMapper
from models.Aircraft import Aircraft
from services.CrudService import CrudService


class AircraftService(CrudService[Aircraft, AircraftMapper, AircraftHelper]):
    pass
