import json


class UnicityChecker:
    @staticmethod
    def check_unique_attribute(file_path, attribute_name):
        unique_values = set()

        with open(file_path) as file:
            datas = json.load(file)

            for data in datas:
                attribute_value = data.get(attribute_name)
                if attribute_value in unique_values:
                    return False
                else:
                    unique_values.add(attribute_value)

        return True
