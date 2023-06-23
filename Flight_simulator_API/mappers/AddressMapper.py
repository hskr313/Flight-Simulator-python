from models.Address import Address
from mappers.BaseMapper import BaseMapper


class AddressMapper:
    """
    This class serves as a mapper for Address objects, providing static methods to convert Address objects to JSON,
    and JSON to Address objects.
    """

    @staticmethod
    def to_json(address: Address):
        """
        Converts an Address object to a dictionary (JSON).

        :param address: Address object to be converted.
        :return: A dictionary representation of the address.
        """
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
        """
        Converts a dictionary (JSON) to an Address object.

        :param address_json: The dictionary representation of an address.
        :return: An Address object created from the dictionary.
        """
        address = Address(
            address_json.get("street"),
            address_json.get("street_number"),
            address_json.get("city"),
            address_json.get("postal_code"),
            address_json.get("country")
        )
        return address
