from mappers.AddressMapper import AddressMapper

class SafeUser:
    """
    The SafeUser class is a safe representation of the User object which excludes sensitive data like password.
    It is used when a representation of the User object needs to be sent to the client.
    """

    def __init__(self, user):
        """
        Initializes a new instance of the SafeUser class.

        :param user: The User object to be converted to a safe representation.
        """
        self.id = user.id
        self.created_at = user.created_at
        self.updated_at = user.updated_at
        self.last_name = user.last_name
        self.first_name = user.first_name
        self.email = user.email
        self.address = AddressMapper.to_json(user.address)
        self.roles = user.roles

    def to_json(self):
        """
        Converts the SafeUser object to a dictionary that can be easily converted to JSON.

        :return: A dictionary representing the SafeUser object.
        """
        return self.__dict__
