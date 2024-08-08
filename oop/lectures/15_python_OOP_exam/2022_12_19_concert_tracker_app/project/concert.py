from project.validation.validation import Validation


class Concert:
    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    @property
    def concert_genre(self):
        return ["Metal", "Rock", "Jazz"]

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        Validation.validate_ganre_or_music(value,self.concert_genre, f"Our group doesn't play {value}!" )
        self.__genre = value


    @property
    def audience(self):
        return self.__audience

    @audience.setter
    def audience(self, value):
        Validation.valid_number(value, 1, "At least one person should attend the concert!")
        self.__audience = value

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        Validation.valid_number(value, 1, "Ticket price must be at least 1.00$!")
        self.__ticket_price = value
    
    
    @property
    def expenses(self):
        return self.__expenses
    
    @expenses.setter
    def expenses(self, value):
        Validation.valid_number(value, 0, "Expenses cannot be a negative number!")
        self.__expenses = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        Validation.valid_str_or_white_space(value, 2, "Place must contain at least 2 chars. It cannot be empty!")
        self.__place = value

    def __str__(self):
        return f"{self.genre} concert at {self.place}."
