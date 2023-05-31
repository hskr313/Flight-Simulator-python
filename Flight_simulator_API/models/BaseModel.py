from datetime import datetime


class BaseModel:

    def __init__(self):
        self.id = 0
        self.created_at = datetime.now()
        self.updated_at = self.created_at
