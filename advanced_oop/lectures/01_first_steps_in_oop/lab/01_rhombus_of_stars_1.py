""" 1 """

n = int(input())


def print_row(size, row):
    empty = " "
    star = "* "
    print(f"{empty * (size - row)}{star * row}")


def print_upper_part(size):
    for row in range(1, size):
        print_row(size, row)


def print_center_part(size):
    print_row(size, size)


def print_bottom_part(size):
    for row in range(size - 1, 0, -1):
        print_row(size, row)


def print_rhumbus(size):
    print_upper_part(size)
    print_center_part(size)
    print_bottom_part(size)


print_rhumbus(n)

""" 2 """


class InputData:
    def __init__(self) -> None:
        self.n: int = int(input())


class PrintRow:
    def print_row(self, size: int, row: int) -> None:
        empty: str = " "
        star: str = "* "
        print(f"{empty * (size - row)}{star * row}")


class RhombusParts:
    def __init__(self, size: int, print_row_obj: PrintRow) -> None:
        self.size: int = size
        self.print_row_obj: PrintRow = print_row_obj

    def print_upper_part(self) -> None:
        for row in range(1, self.size):
            self.print_row_obj.print_row(self.size, row)

    def print_center_part(self) -> None:
        self.print_row_obj.print_row(self.size, self.size)

    def print_bottom_part(self) -> None:
        for row in range(self.size - 1, 0, -1):
            self.print_row_obj.print_row(self.size, row)


class RhombusPrinter:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.print_row_obj: PrintRow = PrintRow()
        self.rhombus_parts: RhombusParts = RhombusParts(size, self.print_row_obj)

    def print_rhombus(self) -> None:
        self.rhombus_parts.print_upper_part()
        self.rhombus_parts.print_center_part()
        self.rhombus_parts.print_bottom_part()


input_data: InputData = InputData()
rhombus_printer: RhombusPrinter = RhombusPrinter(input_data.n)
rhombus_printer.print_rhombus()
