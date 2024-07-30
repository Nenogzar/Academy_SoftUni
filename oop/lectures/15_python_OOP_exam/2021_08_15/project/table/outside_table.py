from project.table.table import Table
from project.validators import *


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
        validate_table_number(value, self.MIN, self.MAX, "Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value
