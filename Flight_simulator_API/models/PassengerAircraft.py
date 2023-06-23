from models.Aircraft import Aircraft


class PassengerAircraft(Aircraft):
    """
    The PassengerAircraft class represents an aircraft designed to carry passengers.
    It extends the Aircraft class with additional attributes related to passenger capacity.

    Attributes:
        business_capacity: The maximum number of business-class passengers the aircraft can carry.
        economy_capacity: The maximum number of economy-class passengers the aircraft can carry.
    """

    def __init__(self, model, company_name, max_speed, fuel_tank, business_capacity, economy_capacity):
        """
        Initializes a new instance of the PassengerAircraft class.

        :param model: The model of the aircraft.
        :param company_name: The name of the company that owns the aircraft.
        :param max_speed: The maximum speed of the aircraft.
        :param fuel_tank: The fuel tank capacity of the aircraft.
        :param business_capacity: The maximum number of business-class passengers the aircraft can carry.
        :param economy_capacity: The maximum number of economy-class passengers the aircraft can carry.
        """
        super().__init__(model, company_name, max_speed, fuel_tank)
        self.business_capacity = business_capacity
        self.economy_capacity = economy_capacity
