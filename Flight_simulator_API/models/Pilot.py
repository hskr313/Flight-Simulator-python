from models.User import User


class Pilot(User):
    """
    The Pilot class represents a user that has pilot credentials.
    It extends the User class with an additional attribute related to the pilot's license number.

    Attributes:
        license_number: The pilot's license number.
    """

    def __init__(self, last_name, first_name, email, password, address, roles, license_number):
        """
        Initializes a new instance of the Pilot class.

        :param last_name: The last name of the user.
        :param first_name: The first name of the user.
        :param email: The email address of the user.
        :param password: The password for the user.
        :param address: The address of the user.
        :param roles: The roles assigned to the user.
        :param license_number: The pilot's license number.
        """
        super().__init__(last_name, first_name, email, password, address, roles)
        self.license_number = license_number
