from abc import ABC
from typing import TypeVar, Generic, List

from JsonHelpers.BaseHelper import BaseHelper
from mappers.BaseMapper import BaseMapper

T = TypeVar('T')
Mapper = TypeVar('Mapper', bound=BaseMapper)
Helper = TypeVar('Helper', bound=BaseHelper)


class CrudService(Generic[T, Mapper, Helper], ABC):
    """
    A generic CRUD service class for managing entities.

    Args:
        mapper (Mapper): The mapper for mapping entity objects.
        helper (Helper): The helper for performing CRUD operations on entities.
        file_path (str): The file path for storing entity data.
    """

    def __init__(self, mapper: Mapper, helper: Helper, file_path):
        self.mapper = mapper
        self.helper = helper
        self.file_path = file_path

    def read_all(self) -> List[dict]:
        """
        Reads all entities.

        Returns:
            list: A list of all entities.
        """
        return self.helper.read_all(self.file_path)

    def read_one_by_id(self, entity_id) -> dict:
        """
        Reads a single entity by its ID.

        Args:
            entity_id: The ID of the entity.

        Returns:
            object: The retrieved entity.
        """
        return self.helper.read_one_by_id(entity_id, self.file_path)

    def save(self, obj: T) -> T:
        """
        Saves an entity.

        Args:
            obj (object): The entity to be saved.

        Returns:
            object: The saved entity.
        """
        return self.helper.save(obj, self.file_path)

    def delete(self, entity_id) -> None:
        """
        Deletes an entity by its ID.

        Args:
            entity_id: The ID of the entity.
        """
        self.helper.delete(entity_id, self.file_path)
