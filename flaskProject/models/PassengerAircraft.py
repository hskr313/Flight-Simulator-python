from models.Aircraft import Aircraft


class PassengerAircraft(Aircraft):

    def __init__(self, model, status, company_name, max_speed, fuel_tank, number_of_seats):
        super().__init__(model, status, company_name, max_speed, fuel_tank)
        self.number_of_seats = number_of_seats
        