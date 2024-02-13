def perfectNumber(number):
    sum = 0
    for x in range(1, number):
        if number % x == 0:
            sum += x
    return sum == number

if __name__ == '__main__':

    n = int(input("enter a number to check : "))
    print(perfectNumber(n))


def is_perfect_number(num):
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_of_divisors == num


def find_perfect_numbers_in_range(upper_limit):
    perfect_numbers = [num for num in range(1, upper_limit + 1) if is_perfect_number(num)]
    return perfect_numbers


if __name__ == '__main__':
    upper_limit = int(input("Въведете горна граница на положителните числа: "))
    perfect_numbers = find_perfect_numbers_in_range(upper_limit)

    if 0 < upper_limit <= 5:
        print(f"Няма перфектни числа в диапазона до {upper_limit}")
    else:
        print(f"Перфектни числа в диапазона до {upper_limit}: {perfect_numbers}")