from models.BaseModel import BaseModel


class Airport(BaseModel):
    """
    The Airport class represents an airport.
    """

    def __init__(self, name, address, runways, itineraries):
        """
        Initializes a new instance of the Airport class.

        :param name: The name of the airport.
        :param address: The address of the airport.
        :param runways: A list of runways at the airport.
        :param itineraries: A list of itineraries associated with the airport.
        """
    def __init__(self, name, address):
        super().__init__()
        self.name = name
        self.address = address
        # self.runways = runways
        # self.itineraries = itineraries
