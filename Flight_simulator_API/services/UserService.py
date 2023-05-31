from typing import Optional

from mappers.UserMapper import UserMapper
from models.User import User
from utils.UnicityChecker import UnicityChecker
from JsonHelpers.UserHelper import UserHelper


class UserService:
    def __init__(self, user_mapper: UserMapper, user_helper: UserHelper, file_path):
        self.file_path = file_path
        self.user_mapper = user_mapper
        self.user_helper = user_helper

    def get_user_by_email(self, email) -> Optional[User]:
        users = self.user_helper.read_all(self.file_path)
        for user_json in users:
            user = UserMapper.from_json(user_json)
            if user.email == email:
                return user
        return None

    def email_exists(self, email) -> bool:
        return not UnicityChecker.check_unique_attribute(self.file_path, email)


