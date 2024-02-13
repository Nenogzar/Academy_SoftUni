
sum_numbers = int(input()) + int(input())
subtract = sum_numbers - int(input())
print(subtract)

""" 2 """
print((int(input()) + int(input())) - int(input()))

""" function"""
def substract_number(num1, num2, num3):
    sub = (num1 + num2) - num3
    return sub


a, b, c = int(input()), int(input()), int(input())
print(substract_number(a,b,c))


""" """
sum_numbers = lambda num1, num2: num1 + num2
subtract = lambda result, num3: result - num3
add_and_subtract = lambda num1, num2, num3: subtract(sum_numbers(num1, num2), num3)
num1, num2, num3 = int(input()), int(input()), int(input())
print(add_and_subtract(num1, num2, num3))