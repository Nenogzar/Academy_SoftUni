from icecream import ic

numbers = list(range(-5, 6))
# numbers = [num for num in range(-25, 26)]

ic(numbers)
def square_num(num):
    if num % 2 == 0:
        return num ** 2
    return num ** 3

ic(list(map(square_num, numbers)))


def comparing(num):
    negativ, positive = [], []

    for n in num:
        if n < 0:
            negativ.append(n)
        else:
            positive.append(n)

    return [positive, negativ]


ic(comparing(numbers))


def multi_number(number):
    return number * number

ic(list(map(multi_number,numbers)))




def multi_number(numbers):
    result = []
    for i in range(len(numbers) - 1):
        result.append(numbers[i] * numbers[i+1])
        # ic(numbers[i], "*", numbers[i + 1])
    return result

ic(multi_number(numbers))


""" str to int and str to float"""

list_str = "1.2", "-3.5", "0", "5", "12.33", "14"

def safe_int_conversion(value):
    try:
        return int(value)
    except ValueError:
        ic(f"Could not convert {value} to int.")
        return None

ic(list(filter(None, map(safe_int_conversion, list_str))))


def safe_float_conversion(value):
    try:
        return float(value)
    except ValueError:
        ic(f"Could not convert {value} to int.")
        return None
float_list = []
ic(list(filter(None, map(safe_float_conversion, list_str))))

