from typing import Optional, List

from JsonHelpers.BaseHelper import BaseHelper, T
from models.Booking import Booking


class BookingHelper(BaseHelper[Booking]):
    """
    Helper class for operations related to Booking data storage and retrieval.
    This class extends BaseHelper and inherits all its methods.
    """

    def save(self, obj: T, file_path) -> Booking:
        """
        Save a booking object to a file.

        :param obj: The booking object to be saved.
        :param file_path: The file path where the booking data is to be saved.
        :return: The saved booking object.
        """
        return super().save(obj, file_path)

    def read_all(self, file_path) -> List[dict]:
        """
        Read all bookings data from a file.

        :param file_path: The file path where the bookings data is stored.
        :return: A list of booking data in dictionary format.
        """
        return super().read_all(file_path)

    def read_one_by_id(self, entity_id: int, file_path) -> Optional[dict]:
        """
        Read one booking data by its ID from a file.

        :param entity_id: The ID of the booking to be read.
        :param file_path: The file path where the bookings data is stored.
        :return: The booking data in dictionary format or None if not found.
        """
        return super().read_one_by_id(entity_id, file_path)

    def delete(self, entity_id: int, file_path) -> None:
        """
        Delete a booking by its ID from a file.

        :param entity_id: The ID of the booking to be deleted.
        :param file_path: The file path where the bookings data is stored.
        """
        super().delete(entity_id, file_path)
