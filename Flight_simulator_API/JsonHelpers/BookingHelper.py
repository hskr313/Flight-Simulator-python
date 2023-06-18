from typing import Optional, List

from JsonHelpers.BaseHelper import BaseHelper, T
from models.Booking import Booking


class BookingHelper(BaseHelper[Booking]):
    def save(self, obj: T, file_path) -> Booking:
        return super().save(obj, file_path)

    def read_all(self, file_path) -> List[dict]:
        return super().read_all(file_path)

    def read_one_by_id(self, entity_id: int, file_path) -> Optional[dict]:
        return super().read_one_by_id(entity_id, file_path)

    def delete(self, entity_id: int, file_path) -> None:
        super().delete(entity_id, file_path)
