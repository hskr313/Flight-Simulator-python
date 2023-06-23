from models.BaseModel import BaseModel


class User(BaseModel):
    """
    The User class represents a user in the system. It inherits from the BaseModel class.

    Attributes:
        last_name: The last name of the user.
        first_name: The first name of the user.
        email: The email address of the user.
        password: The password for the user.
        address: The address of the user.
        roles: The roles assigned to the user.
    """

    def __init__(self, last_name, first_name, email, password, address, roles):
        """
        Initializes a new instance of the User class.

        :param last_name: The last name of the user.
        :param first_name: The first name of the user.
        :param email: The email address of the user.
        :param password: The password for the user.
        :param address: The address of the user.
        :param roles: The roles assigned to the user.
        """
        super().__init__()
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.password = password
        self.address = address
        self.roles = roles
