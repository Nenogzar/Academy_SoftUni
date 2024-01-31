# input_numbers = input()
#
# rounded_numbers = [round(float(num)) for num in input_numbers.split()]
#
# print(rounded_numbers)


#

number = input()

def round_func(string):
    rounded_numbers = []
    for num in string.split():
        rounded_numbers.append(round(float(num)))
    return rounded_numbers

print(round_func(number))
