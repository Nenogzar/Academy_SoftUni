from project.table.table import Table
from project.Validators.validators import Validation


class OutsideTable(Table):
    MIN = 51
    MAX = 100

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not (self.MIN <= value <= self.MAX):
            raise ValueError(f"Outside table's number must be between {self.MIN} and {self.MAX} inclusive!")
        self.__table_number = value
