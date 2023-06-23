from enum import Enum


class Roles(Enum):
    """
    The Roles class is an Enum representing the various roles a user can have in the system.

    Attributes:
        USER: Represents a regular user role.
        ADMIN: Represents an admin user role.
        PILOT: Represents a pilot user role.
    """

    USER = 1
    ADMIN = 2
    PILOT = 3
