number = int(input())
perfect_num = 0

for n in range(1, number):
    if n != 0 and number % n == 0:
        perfect_num += n

if perfect_num == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

""" 2 """

def perfectNumber(number):
    sum = 0
    for x in range(1, number):
        if number % x == 0:
            sum += x
    return "We have a perfect number!" if sum == number else "It's not so perfect."


result = perfectNumber(int(input()))
print(result)

""" 3 """
def is_perfect_number(number):
    divisors_sum = 0

    for divisior in range(1, number):
        if number % divisior == 0:
            divisors_sum += divisior

    if divisors_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(is_perfect_number(num))