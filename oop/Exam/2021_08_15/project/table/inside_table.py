from project.table.table import Table
from project.validators import *


class InsideTable(Table):
    MIN = 1
    MAX = 50

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return

    @table_number.setter
    def table_number(self, value):
        validate_table_number(value, self.MIN, self.MAX, "Inside table's number must be between 1 and 50 inclusive!")
        self.__table_number = value


