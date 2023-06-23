# from models.BaseModel import BaseModel
#
#
# class Runway(BaseModel):
#
#     def __init__(self):
#         super().__init__()
#         self.available = True
from models.BaseModel import BaseModel


class Runway(BaseModel):
    """
    The Runway class represents a runway at an airport. It inherits from the BaseModel class.

    Attributes:
        available: A boolean indicating the availability of the runway.
    """

    def __init__(self):
        """
        Initializes a new instance of the Runway class.
        """
        super().__init__()
        self.available = True
