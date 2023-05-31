from models.BaseModel import BaseModel


class Aircraft(BaseModel):

    def __init__(self, model, available, company_name, max_speed, fuel_tank):
        super().__init__()
        self.model = model
        self.available = available
        self.company_name = company_name
        self.max_speed = max_speed
        self.fuel_tank = fuel_tank
