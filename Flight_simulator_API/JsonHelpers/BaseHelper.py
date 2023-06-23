from typing import TypeVar, Generic, List, Optional
from mappers.BaseMapper import BaseMapper
import time
from abc import ABC
import json

T = TypeVar('T')


class BaseHelper(Generic[T], ABC):

    def __init__(self, mapper: BaseMapper):
        """
        Initializes the BaseHelper class with a given mapper.

        :param mapper: A mapper object that provides methods to convert to and from JSON.
        """
        self.mapper = mapper

    def save(self, obj: T, file_path) -> T:
        """
        Saves an object to a JSON file. If the object doesn't exist, it adds it to the file. If it does exist,
        it updates the object.

        :param obj: The object to be saved.
        :param file_path: The path of the file where the object will be saved.
        :return: The saved object.
        :raises Exception: If there's an error during the save operation.
        """
        try:
            with open(file_path, "r+") as f:
                datas = json.load(f)

                new_obj = self.mapper.to_json(obj)

                if new_obj["id"] is None:
                    new_obj["id"] = max(data["id"] for data in datas) + 1 if datas else 1
                    new_obj["created_at"] = new_obj["updated_at"] = int(time.time())

                for i, data in enumerate(datas):
                    if data["id"] == new_obj["id"]:
                        for key in new_obj:
                            if key != 'id':
                                data[key] = new_obj[key]
                                new_obj["updated_at"] = int(time.time())
                        break
                else:
                    datas.append(new_obj)


                f.seek(0)
                json.dump(datas, f, indent=4)
                f.truncate()
            return self.mapper.from_json(new_obj)
        except Exception:
            raise Exception("Error occurred during save operation")

    def read_all(self, file_path) -> List[dict]:
        """
            Reads all objects from a JSON file.

            :param file_path: The path of the file from where the objects will be read.
            :return: A list of all objects.
            :raises FileNotFoundError: If the file does not exist.
        """
        try:
            with open(file_path, "r") as f:
                datas = json.load(f)
            return datas
        except FileNotFoundError:
            return []

    def read_one_by_id(self, entity_id: int, file_path) -> Optional[dict]:
        """
        Reads a specific object from a JSON file based on its ID.

        :param entity_id: The ID of the object to be read.
        :param file_path: The path of the file from where the object will be read.
        :return: The object that matches the ID.
        :raises Exception: If the object is not found.
        """
        try:
            with open(file_path, "r") as f:
                datas = json.load(f)
                for data in datas:
                    if data['id'] == entity_id:
                        return data
        except Exception:
            raise Exception("Object not found")

    def delete(self, entity_id: int, file_path) -> None:
        """
        Deletes a specific object from a JSON file based on its ID.

        :param entity_id: The ID of the object to be deleted.
        :param file_path: The path of the file from where the object will be deleted.
        :raises Exception: If the object could not be deleted.
        """
        try:
            with open(file_path, "r+") as f:
                datas = json.load(f)

                for i, data in enumerate(datas):
                    if data['id'] == entity_id:
                        del datas[i]

                f.seek(0)
                json.dump(datas, f, indent=4)
                f.truncate()
        except Exception:
            raise Exception("Could not delete element")
