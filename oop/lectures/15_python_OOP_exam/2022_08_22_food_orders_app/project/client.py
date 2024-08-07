from project.validation.validation import Validation


class Client:
    _length_phone_number = 10

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []  # contain all meals (objects) added by the client
        self.order = {}
        self.bill = 0.00

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        Validation.valid_phone_number(value, self._length_phone_number, "Invalid phone number!")
        self.__phone_number = value

    def reset_client_order(self):
        self.shopping_cart = []
        self.order = {}
        self.bill = 0
