number = int(input())
even_sum = 0
odd_sum = 0

# Convert the number to a string to iterate through each character
for digit in str(number):
    num = int(digit)
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

"""2"""

number = int(input())
odd_sum = sum(int(digit) for digit in str(number) if int(digit) % 2 != 0)
even_sum = sum(int(digit) for digit in str(number) if int(digit) % 2 == 0)

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


""" """
def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0

    for digit in str(number):

        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = int(input())
print(odd_even_sum(number))