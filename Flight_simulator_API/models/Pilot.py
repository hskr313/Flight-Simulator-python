from models.User import User


class Pilot(User):
    def __init__(
        self, last_name, first_name, email, password, address, roles, license_number
    ):
        super().__init__(last_name, first_name, email, password, address, roles)
        self.license_number = license_number
