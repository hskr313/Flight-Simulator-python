from models.User import User
from models.Pilot import Pilot
from mappers.BaseMapper import BaseMapper
from mappers.AddressMapper import AddressMapper


class UserMapper(BaseMapper[User]):

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
            "address": AddressMapper.to_json(user.address),
            "roles": [role for role in user.roles]
        }

        if isinstance(user, Pilot):
            user_json["license_number"] = user.license_number

        return user_json

    @staticmethod
    def from_json(user_json: dict):
        address = AddressMapper.from_json(user_json.get("address"))
        if "license_number" in user_json:
            user = Pilot(
                user_json.get("last_name"),
                user_json.get("first_name"),
                user_json.get("email"),
                user_json.get("password"),
                address,
                user_json.get("roles"),
                user_json.get("license_number")
            )
        else:
            user = User(
                user_json.get("last_name"),
                user_json.get("first_name"),
                user_json.get("email"),
                user_json.get("password"),
                address,
                user_json.get("roles")
            )

        user.id = user_json.get("id")
        user.created_at = user_json.get("created_at")
        user.updated_at = user_json.get("updated_at")
        return user
