import math

figures = input()
lice = 0

if figures == "square":
    a = float(input())
    lice = a * a

elif figures == "rectangle":
    a = float(input())
    b = float(input())
    lice = a*b

elif figures == "circle":
    a = float(input())
    lice = math.pi * a**2
else:
    a = float(input())
    b = float(input())
    lice = (a * b)/2
print(f"{lice:.3f}")
