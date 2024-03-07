from prettytable import PrettyTable

def read_date(input_text: str) -> tuple[int, int, int]:
    date_str = input(input_text)
    try:
        day, month, year = map(int, date_str.split('/'))
        return day, month, year
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return None

def display_date(day: int, month: int, year: int) -> None:
    formatted_date = f"{day:02d}/{month:02d}/{year:04d}"
    print(f"Formatted date: {formatted_date}")

def display_date_in_words(day: int, month: int, year: int) -> None:
    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    formatted_date = f"{month_names[month - 1]} {day}, {year}"
    print(f"Formatted date in words: {formatted_date}")

def is_valid_date(day: int, month: int, year: int) -> bool:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= month <= 12:
        days = days_in_month[month - 1]
        if month == 2 and is_leap_year(year):
            days = 29
        if 1 <= day <= days:
            return True

    return False

def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def add_days_to_date(day: int, month: int, year: int, days_to_add: int) -> tuple[int, int, int]:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while days_to_add > 0:
        days_in_year = 366 if is_leap_year(year) else 365
        days_in_current_month = days_in_month[month - 1] - day + 1

        if days_in_current_month <= days_to_add:
            month += 1
            days_to_add -= days_in_current_month
            day = 1
        else:
            day += days_to_add
            days_to_add = 0

        if month > 12:
            month = 1
            year += 1

    return day, month, year

def calculate_difference_in_years(day1: int, month1: int, year1: int,
                                   day2: int, month2: int, year2: int) -> int:
    difference = abs(year1 - year2)
    if month1 < month2 or (month1 == month2 and day1 < day2):
        difference -= 1
    return difference

def visualize_table(header, data):
    table = PrettyTable()
    table.field_names = header
    table.add_row(data)
    print(table)

# Main program
date1 = read_date("Enter date 1 (dd/mm/yyyy): ")
date2 = read_date("Enter date 2 (dd/mm/yyyy): ")

if date1 and date2:
    display_date(*date1)
    display_date_in_words(*date1)

    if is_valid_date(*date1):
        print("Date 1 is valid.")

        days_to_add = int(input("Enter the number of days to add: "))
        new_date = add_days_to_date(*date1, days_to_add)
        display_date(*new_date)
        display_date_in_words(*new_date)

        difference_years = calculate_difference_in_years(*date1, *date2)
        print(f"Difference in years between date 1 and date 2: {difference_years}")

        # Visualize in table format
        visualize_table(["Day", "Month", "Year"], list(date1))
        visualize_table(["Day", "Month", "Year"], list(new_date))

    else:
        print("Date 1 is not valid.")

    if is_valid_date(*date2):
        print("Date 2 is valid.")
    else:
        print("Date 2 is not valid.")
