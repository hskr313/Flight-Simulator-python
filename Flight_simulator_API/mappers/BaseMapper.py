from typing import TypeVar, Generic
from abc import ABC,abstractmethod

T = TypeVar('T')


class BaseMapper(Generic[T], ABC):
    @abstractmethod
    def to_json(self, obj: T):
        pass

    @abstractmethod
    def from_json(self, obj: dict):
        pass
