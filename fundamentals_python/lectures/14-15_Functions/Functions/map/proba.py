from icecream import ic

numbers = list(range(-5, 6))
# numbers = [num for num in range(-25, 26)]


def info_number(num):
    if num % 2 == 0:
        return num ** 2
    return num ** 3


info_fun = map(info_number, numbers)

print(list(info_fun))

number = list(range(-5, 6))


def comparing(num):
    negativ, positive = [], []

    for n in num:
        if n < 0:
            negativ.append(n)
        else:
            positive.append(n)

    return [positive, negativ]


comparing_list = comparing(numbers)

print(comparing_list)
