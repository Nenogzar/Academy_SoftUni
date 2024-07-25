from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    equipment_properties = {
        'ElbowPad': {'PROTECTION': 90, 'PRICE': 25.0, 'INCREASES_PRICE': 1.1},
        'KneePad': {'PROTECTION': 120, 'PRICE': 15.0, 'INCREASES_PRICE': 1.2}
    }

    def __init__(self, protection: int = None, price: float = None):
        class_name = self.__class__.__name__


        self._protection = self.equipment_properties[class_name]['PROTECTION']
        self._price = self.equipment_properties[class_name]['PRICE']

    def increase_price(self) -> None:
        class_name = self.__class__.__name__
        increase_factor = self.equipment_properties[class_name]['INCREASES_PRICE']
        self._price *= increase_factor

    @property
    def protection(self):
        return self._protection

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
