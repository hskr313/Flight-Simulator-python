from typing import List, Optional

from JsonHelpers.BaseHelper import BaseHelper, T
from mappers import UserMapper
from models.User import User


class UserHelper(BaseHelper[User]):

    def __init__(self, mapper: UserMapper):
        super().__init__(mapper)

    def save(self, obj: User, file_path) -> User:
        return super().save(obj, file_path)

    def read_all(self, file_path) -> List[dict]:
        return super().read_all(file_path)

    def read_one_by_id(self, user_id: int, file_path) -> Optional[dict]:
        return super().read_one_by_id(user_id, file_path)

    def delete(self, user_id: int, file_path) -> None:
        super().delete(user_id, file_path)


