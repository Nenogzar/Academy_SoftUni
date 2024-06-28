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
