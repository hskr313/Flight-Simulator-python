from models.BaseModel import BaseModel


class Runway(BaseModel):

    def __init__(self, current_aircraft):
        super().__init__()
        self.current_aircraft = current_aircraft if current_aircraft else None
