from flask_bcrypt import Bcrypt


class AuthService:
    def __init__(self):
        self.bcrypt = Bcrypt()

    def hash_password(self, password) -> str:
        return self.bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password_hash(self, hashed_password, password) -> bool:
        return self.bcrypt.check_password_hash(hashed_password, password)
