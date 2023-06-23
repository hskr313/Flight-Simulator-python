from typing import Optional

from flask import request

from mappers.UserMapper import UserMapper
from models.User import User
from services.CrudService import CrudService, Helper, Mapper
from utils.UnicityChecker import UnicityChecker
from JsonHelpers.UserHelper import UserHelper


class UserService(CrudService[User, UserMapper, UserHelper]):
    """
    A service class for managing users.

    Args:
        mapper (Mapper): The mapper for mapping user objects.
        helper (Helper): The helper for performing CRUD operations on users.
        file_path (str): The file path for storing user data.
    """

    def __init__(self, mapper: Mapper, helper: Helper, file_path):
        super().__init__(mapper, helper, file_path)

    def save_user(self, user_id=None):
        """
        Saves a user.

        Args:
            user_id (str, optional): The ID of the user. Defaults to None.

        Returns:
            dict: The JSON representation of the saved user.
        """
        user_json = request.get_json()
        user = self.mapper.from_json(user_json)
        if user_id:
            user.id = user_id
        user = self.helper.save(user, self.file_path)
        user_json = self.mapper.to_json(user)

        return user_json

    def get_user_by_email(self, email) -> Optional[User]:
        """
        Retrieves a user by email.

        Args:
            email (str): The email address of the user.

        Returns:
            User: The user object if found, None otherwise.
        """
        users = self.helper.read_all(self.file_path)
        for user_json in users:
            user = self.mapper.from_json(user_json)
            if user.email == email:
                return user
        return None

    def email_exists(self, email) -> bool:
        """
        Checks if an email already exists in the user data.

        Args:
            email (str): The email address to check.

        Returns:
            bool: True if the email exists, False otherwise.
        """
        return not UnicityChecker.check_unique_attribute(self.file_path, 'email', email)
