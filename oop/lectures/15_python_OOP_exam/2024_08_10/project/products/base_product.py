from abc import ABC, abstractmethod

from project.valaidation.validation import Validation


class BaseProduct(ABC):
    def __init__(self, model: str, price: float, material: str, sub_type: str):
        self.model = model
        self.price = price
        self.material = material
        self.sub_type = sub_type



    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validation.validate_len_white_space(value,3,"Product model must be at least 3 chars long!")
        self.__model = value
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        Validation.validate_les_or_equal(value, 0,"Product price must be greater than zero!")
        self.__price = value

    @abstractmethod
    def discount(self):
        pass

    @abstractmethod
    def get_sub_type(self):
        pass
