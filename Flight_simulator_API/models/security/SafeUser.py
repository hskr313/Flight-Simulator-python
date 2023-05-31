class SafeUser:
    def __init__(self, user):
        self.id = user.id
        self.created_at = user.created_at
        self.updated_at = user.updated_at
        self.last_name = user.last_name
        self.first_name = user.first_name
        self.email = user.email
        self.address = user.address
        self.roles = user.roles

    def to_json(self):
        return self.__dict__
