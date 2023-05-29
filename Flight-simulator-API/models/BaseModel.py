import uuid
from datetime import datetime


class BaseModel:

    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = self.created_at
