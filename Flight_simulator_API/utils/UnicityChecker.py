import json


class UnicityChecker:
    @staticmethod
    def check_unique_attribute(file_path, attribute_name, attribute_value):
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
