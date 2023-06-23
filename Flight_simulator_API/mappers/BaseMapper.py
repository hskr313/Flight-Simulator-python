from typing import TypeVar, Generic
from abc import ABC,abstractmethod

T = TypeVar('T')


class BaseMapper(Generic[T], ABC):
    """
    This is an abstract base class that provides the blueprint for specific mapper classes.
    The base mapper defines two abstract methods: to_json and from_json, which must be implemented in any child class.
    """

    @abstractmethod
    def to_json(self, obj: T):
        """
        This abstract method defines the structure for converting an object to a dictionary (JSON).
        It must be implemented in any child class.

        :param obj: The object to be converted to a dictionary.
        """
        pass

    @abstractmethod
    def from_json(self, obj: dict):
        """
        This abstract method defines the structure for converting a dictionary (JSON) to an object.
        It must be implemented in any child class.

        :param obj: The dictionary to be converted to an object.
        """
        pass
