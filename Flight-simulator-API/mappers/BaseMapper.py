from typing import TypeVar, Generic

T = TypeVar('T')


class BaseMapper(Generic[T]):
    @staticmethod
    def to_json(obj: T):
        pass

    @staticmethod
    def from_json(obj: T):
        pass
