from models.User import User
from models.Pilot import Pilot
from mappers.BaseMapper import BaseMapper


class UserMapper(BaseMapper):

    @staticmethod
    def to_json(user: User):
        user_json = {
            "id": user.id,
            "created_at": user.created_at,
            "updated_at": user.updated_at,
            "last_name": user.last_name,
            "first_name": user.first_name,
            "email": user.email,
            "password": user.password,
            "address": user.address,
            "roles": [role for role in user.roles]
        }

        if isinstance(user, Pilot):
            user_json["license_number"] = user.license_number

        return user_json

    @staticmethod
    def from_json(user_json: dict):
        if "license_number" in user_json:
            user = Pilot(
                user_json["last_name"],
                user_json["first_name"],
                user_json["email"],
                user_json["password"],
                user_json["address"],
                user_json["roles"],
                user_json["license_number"]
            )
        else:
            user = User(
                user_json["last_name"],
                user_json["first_name"],
                user_json["email"],
                user_json["password"],
                user_json["address"],
                user_json["roles"]
            )

        user.id = user_json["id"]
        user.created_at = user_json["created_at"]
        user.updated_at = user_json["updated_at"]
        return user
