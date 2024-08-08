from abc import ABC, abstractmethod

from project.validation.validation import Validation


class BaseService(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots = []  # contain robots (objects) added to the service

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.valid_not_empty_not_white_space(value, "Service name cannot be empty!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validation.valid_number(value, 0, "Service capacity cannot be less than or equal to 0!")
        self.__capacity = value

    @abstractmethod
    def details(self):
        pass
