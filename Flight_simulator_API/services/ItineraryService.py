from JsonHelpers.ItineraryHelper import ItineraryHelper
from mappers.ItineraryMapper import ItineraryMapper
from models.Itinerary import Itinerary
from services.CrudService import CrudService


class ItineraryService(CrudService[Itinerary, ItineraryMapper, ItineraryHelper]):
    pass
