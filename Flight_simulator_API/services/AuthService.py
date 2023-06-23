from flask_bcrypt import Bcrypt


class AuthService:
    """
    The AuthService class provides authentication-related functionality, such as password hashing and validation of roles.

    Methods:
        hash_password: Hashes a password using bcrypt.
        check_password_hash: Checks if a password matches its hashed value.
        validate_roles: Validates a list of roles against the allowed roles.

    Attributes:
        bcrypt: An instance of the Bcrypt class for password hashing.
    """

    def __init__(self):
        """
        Initializes a new instance of the AuthService class.
        """
        self.bcrypt = Bcrypt()

    def hash_password(self, password) -> str:
        """
        Hashes a password using bcrypt.

        :param password: The password to hash.
        :return: The hashed password as a string.
        """
        return self.bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password_hash(self, hashed_password, password) -> bool:
        """
        Checks if a password matches its hashed value.

        :param hashed_password: The hashed password to check against.
        :param password: The password to check.
        :return: True if the password matches, False otherwise.
        """
        return self.bcrypt.check_password_hash(hashed_password, password)

    @staticmethod
    def validate_roles(roles) -> bool:
        """
        Validates a list of roles against the allowed roles.

        :param roles: The roles to validate.
        :return: True if all roles are valid, False otherwise.
        """
        allowed_roles = ["USER", "PILOT"]
        return all(role in allowed_roles for role in roles)
