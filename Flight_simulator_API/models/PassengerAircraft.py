from models.Aircraft import Aircraft


class PassengerAircraft(Aircraft):

    def __init__(self, model, company_name, max_speed, fuel_tank, business_capacity, economy_capacity):
        super().__init__(model, company_name, max_speed, fuel_tank)
        self.business_capacity = business_capacity
        self.economy_capacity = economy_capacity
        