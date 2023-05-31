from typing import TypeVar, Generic
from abc import ABC,abstractmethod

T = TypeVar('T')


class BaseMapper(Generic[T], ABC):
    @staticmethod
    @abstractmethod
    def to_json(obj: T):
        pass

    @staticmethod
    @abstractmethod
    def from_json(obj: dict):
        pass
