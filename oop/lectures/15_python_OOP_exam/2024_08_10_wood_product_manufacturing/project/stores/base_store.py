from abc import ABC, abstractmethod

from project.valaidation.validation import Validation


class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.valid_empty_white_space(value, "Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        Validation.three_white_space(value, "Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validation.validate_les_or_equal(value, 0, "Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self):
        total_price = sum(product.price for product in self.products)
        profit = total_price * 0.10
        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"

    @property
    @abstractmethod
    def store_type(self):
        """ Returns the type of the store as a property. """
        pass
    @abstractmethod
    def store_stats(self):
        """•	Returns detailed information about the store."""
        pass
