from models.Address import Address
from mappers.BaseMapper import BaseMapper


class AddressMapper(BaseMapper[Address]):

    @staticmethod
    def to_json(address: Address):
        address_json = {
            "street": address.street,
            "street_number": address.street_number,
            "city": address.city,
            "postal_code": address.postal_code,
            "country": address.country
        }
        return address_json

    @staticmethod
    def from_json(address_json: dict):
        address = Address(
            address_json.get("street"),
            address_json.get("street_number"),
            address_json.get("city"),
            address_json.get("postal_code"),
            address_json.get("country")
        )
        return address

