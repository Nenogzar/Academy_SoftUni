""" 1 """

# factorial = (lambda f: lambda x: x * f(f, x - 1) if x > 0 else 1)(lambda f, x: x * f(f, x - 1) if x > 0 else 1)
# num = int(input("which number you need to make factoriel: "))
# answer = factorial(num)
# print(f"{answer = }")

# (lambda f: lambda x: x * f(f, x - 1) if x > 0 else 1)
def f (f, x):
    if x > 0:
        return x * f (f, x - 1)
    else:
        return 1

# (lambda f, x: x * f(f, x - 1) if x > 0 else 1)
def factorial (x):#     return f (f, x)




result = 1
for number in range(1, num +1 ):
    result *= number
print(f"{result = }")
