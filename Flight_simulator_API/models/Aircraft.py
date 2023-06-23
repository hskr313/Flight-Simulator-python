from models.BaseModel import BaseModel


class Aircraft(BaseModel):
    """
    The Aircraft class represents an aircraft.
    """

    def __init__(self, model, company_name, max_speed, fuel_tank):
        """
        Initializes a new instance of the Aircraft class.

        :param model: The model of the aircraft.
        :param company_name: The name of the company that operates the aircraft.
        :param max_speed: The maximum speed of the aircraft.
        :param fuel_tank: The capacity of the aircraft's fuel tank.
        """
        super().__init__()
        self.model = model
        self.available = True
        self.company_name = company_name
        self.max_speed = max_speed
        self.fuel_tank = fuel_tank
