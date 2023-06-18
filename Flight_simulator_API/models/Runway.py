from models.BaseModel import BaseModel


class Runway(BaseModel):
    def __init__(self):
        super().__init__()
        self.available = True
