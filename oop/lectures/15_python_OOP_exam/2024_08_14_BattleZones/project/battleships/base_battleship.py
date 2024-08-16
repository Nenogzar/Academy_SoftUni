from abc import ABC, abstractmethod


class BaseBattleship(ABC):
    def __init__(self, name: str, health: int, hit_strength: int, ammunition: int):
        self.name = name        #  name of the battleship
        self.health = health    # health of the battleship
        self.hit_strength = hit_strength    # damage the battleship inflicts
        self.ammunition = ammunition        # ammunition of the battleship.
        self.is_attacking = False
        self.is_available = True        # True (not participating)

        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError("Ship name must contain only letters!")
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    def take_damage(self, enemy_battleship: 'BaseBattleship'):
        self.health = max(0, self.health - enemy_battleship.hit_strength)

    @abstractmethod
    def attack(self):
        pass
