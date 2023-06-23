from models.Aircraft import Aircraft

class CargoAircraft(Aircraft):
    """
    CargoAircraft is a subclass of the Aircraft class representing a cargo aircraft.
    It extends the Aircraft class with an additional attribute - 'capacity',
    which represents the cargo carrying capacity of the aircraft.

    Other inherited attributes include 'model', 'company_name', 'max_speed', and 'fuel_tank' from the parent Aircraft class.
    """

    def __init__(self, model, company_name, max_speed, fuel_tank, capacity):
        """
        Initializes a new instance of the CargoAircraft class.
        :param model: Model of the aircraft.
        :param company_name: Name of the aircraft's manufacturing company.
        :param max_speed: Maximum speed of the aircraft.
        :param fuel_tank: Fuel tank capacity of the aircraft.
        :param capacity: Cargo carrying capacity of the aircraft.
        """
        super().__init__(model, company_name, max_speed, fuel_tank)
        self.capacity = capacity
