from project.vadidation.validation import Validation



class Player:
    player_name = []
    min_stamina = 0
    max_stamina = 100

    def __init__(self, name: str, age: int, stamina = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.valid_name(value, "Name not valid!")
        Validation.valid_unic_name(value, Player.player_name, f"Name {value} is already used!")
        self.__name = value
        Player.player_name.append(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validation.valid_age(value, "The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validation.valid_stanima(value, Player.min_stamina, Player.max_stamina, "Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < self.max_stamina

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
