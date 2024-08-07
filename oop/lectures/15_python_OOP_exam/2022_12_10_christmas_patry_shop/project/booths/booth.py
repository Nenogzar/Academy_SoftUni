from abc import ABC, abstractmethod

from project.valaidation.validation import Validation


class Booth(ABC):
    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []   # contain delicacies (objects) that are ordered
        self.price_for_reservation = 0.00
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validation.positiv_number(value, "Capacity cannot be a negative number!")
        self.__capacity = value

    @abstractmethod
    def reserve(self,number_of_people: int):
        pass
