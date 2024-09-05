from abc import ABC, abstractmethod


class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code = code  # code of the zone
        self.volume = volume  # zone's volume (capacity)
        self.ships = []  # containing battleships (objects) each zone has

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code = value

    def get_ships(self):
        return sorted(self.ships, key=lambda ship: (-ship.hit_strength, ship.name))

    @abstractmethod
    def zone_info(self):
        pass