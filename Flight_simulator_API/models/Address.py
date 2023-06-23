class Address:
    """
    The Address class represents a geographical address.
    """

    def __init__(self, street, street_number, city, postal_code, country):
        """
        Initializes a new instance of the Address class.

        :param street: The street name of the address.
        :param street_number: The street number of the address.
        :param city: The city of the address.
        :param postal_code: The postal code of the address.
        :param country: The country of the address.
        """
        self.street = street
        self.street_number = street_number
        self.city = city
        self.postal_code = postal_code
        self.country = country
