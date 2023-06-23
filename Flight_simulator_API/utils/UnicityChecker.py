import json


class UnicityChecker:
    """
    A utility class for checking the uniqueness of an attribute in a JSON file.
    """

    @staticmethod
    def check_unique_attribute(file_path, attribute_name, attribute_value):
        """
        Checks if the attribute value is unique in the JSON file.

        Args:
            file_path (str): The file path of the JSON file.
            attribute_name (str): The name of the attribute to check for uniqueness.
            attribute_value (Any): The value of the attribute to check.

        Returns:
            bool: True if the attribute value is unique, False otherwise.
        """
        unique_values = set()

        with open(file_path) as file:
            datas = json.load(file)

            for data in datas:
                if attribute_name in data:
                    current_value = data.get(attribute_name)
                    if current_value == attribute_value:
                        return False
                    else:
                        unique_values.add(current_value)

        return True
