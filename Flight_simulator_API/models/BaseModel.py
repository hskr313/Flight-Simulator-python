from datetime import datetime


class BaseModel:
    """
    BaseModel is the base class for other models in the application.
    It provides common attributes that are shared across models.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        Sets the 'id', 'created_at' and 'updated_at' attributes to their default values.
        """
        self.id = None
        self.created_at = datetime.now()
        self.updated_at = self.created_at
