from abc import ABC
from typing import TypeVar, Generic

from JsonHelpers.BaseHelper import BaseHelper
from mappers.BaseMapper import BaseMapper

T = TypeVar('T')
Mapper = TypeVar('Mapper', bound=BaseMapper)
Helper = TypeVar('Helper', bound=BaseHelper)


class CrudService(Generic[T, Mapper, Helper], ABC):

    def __init__(self, mapper: Mapper, helper: Helper, file_path):
        self.mapper = mapper
        self.helper = helper
        self.file_path = file_path

    def read_all(self):
        return self.helper.read_all(self.file_path)

    def read_one_by_id(self, entity_id):
        return self.helper.read_one_by_id(entity_id, self.file_path)

    def save(self, obj: T):
        return self.helper.save(obj, self.file_path)

    def delete(self, entity_id):
        self.helper.delete(entity_id, self.file_path)
