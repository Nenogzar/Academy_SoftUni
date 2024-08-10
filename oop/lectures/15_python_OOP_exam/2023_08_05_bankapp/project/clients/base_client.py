from abc import ABC,abstractmethod

from project.validation.validation import Validation


class BaseClient(ABC):
    def __init__(self, name: str, client_id: str, income: float, interest: float):
        self.name = name        # name of the client
        self.client_id = client_id  # id number of a client
        self.income = income        # income of a client
        self.interest = interest    # client’s interest
        self.loans = []             # contain loans (objects) each client


    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        Validation.vaid_empty_white_space(value, "Client name cannot be empty!")
        self.__name = value
    
    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        Validation.valid_10_symbols(value, "Client ID should be 10 symbols long!")
        self.__client_id = value

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, value):
        Validation.value_positiv_number(value, "Income must be greater than zero!")
        self.__income = value

    @abstractmethod
    def increase_clients_interest(self):
        pass
