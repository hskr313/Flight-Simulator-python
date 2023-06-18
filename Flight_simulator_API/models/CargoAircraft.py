from models.Aircraft import Aircraft


class CargoAircraft(Aircraft):
    def __init__(self, model, company_name, max_speed, fuel_tank, capacity):
        super().__init__(model, company_name, max_speed, fuel_tank)
        self.capacity = capacity
