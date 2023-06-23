from typing import List, Optional

from JsonHelpers.BaseHelper import BaseHelper, T
from mappers import UserMapper
from models.User import User


class UserHelper(BaseHelper[User]):
    """
    Helper class for operations related to User data storage and retrieval.
    This class extends BaseHelper and inherits all its methods.
    """

    def __init__(self, mapper: UserMapper):
        """
        Initializes the UserHelper with a specific UserMapper.

        :param mapper: A UserMapper object used for mapping between User objects and dictionaries.
        """
        super().__init__(mapper)

    def save(self, obj: User, file_path) -> User:
        """
        Save a User object to a file.

        :param obj: The User object to be saved.
        :param file_path: The file path where the User data is to be saved.
        :return: The saved User object.
        """
        return super().save(obj, file_path)

    def read_all(self, file_path) -> List[dict]:
        """
        Read all User data from a file.

        :param file_path: The file path where the User data is stored.
        :return: A list of User data in dictionary format.
        """
        return super().read_all(file_path)

    def read_one_by_id(self, user_id: int, file_path) -> Optional[dict]:
        """
        Read one User data by its ID from a file.

        :param user_id: The ID of the User to be read.
        :param file_path: The file path where the User data is stored.
        :return: The User data in dictionary format or None if not found.
        """
        return super().read_one_by_id(user_id, file_path)

    def delete(self, user_id: int, file_path) -> None:
        """
        Delete a User by its ID from a file.

        :param user_id: The ID of the User to be deleted.
        :param file_path: The file path where the User data is stored.
        """
        super().delete(user_id, file_path)
