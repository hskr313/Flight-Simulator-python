from models.BaseModel import BaseModel


class Airport(BaseModel):
    def __init__(self, name, address, runways, itineraries):
        super().__init__()
        self.name = name
        self.address = address
        self.runways = runways
        self.itineraries = itineraries
