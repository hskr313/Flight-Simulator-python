from typing import TypeVar, Generic, List
from mappers.BaseMapper import BaseMapper

T = TypeVar('T')


class BaseHelper(Generic[T]):

    def __init__(self, mapper: BaseMapper):
        self.mapper = mapper

    def create(self, obj: T, file_name) -> T:

        self.mapper.to_json(obj)
        return obj

    def read_all(self,) -> T:

        pass

    def update(self, item: T) -> T:

        pass

    def delete(self, id: int) -> None:

        pass
