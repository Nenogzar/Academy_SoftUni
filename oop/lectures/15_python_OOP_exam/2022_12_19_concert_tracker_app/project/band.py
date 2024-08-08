from project.validation.validation import Validation


class Band:
    def __init__(self, name: str):
        self.name = name
        self.members = []  # contain the members (musician objects) of the band

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validation.valid_str_or_white_space(value, 1, "Band name should contain at least one character!")
        self.__name = value

    def __str__(self):
        return f"{self.__name} with {len(self.members)} members."
