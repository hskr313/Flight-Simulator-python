from models.BaseModel import BaseModel


class User(BaseModel):
    def __init__(self, last_name, first_name, email, password, address, roles):
        super().__init__()
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.password = password
        self.address = address
        self.roles = roles
