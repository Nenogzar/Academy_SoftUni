n1 = int(input())
n2 = int(input())
oper = input("+ - * / %")
result = 0
num_type = ""
output = " "

if n2 == 0 and (oper == "/" or oper == "%"):
    print(f" Connot divide {n1} by {n2}")
elif oper == "/":
    result = n1 / n2
    print(f"{n1} {oper} {n2} = {result:.2f}")
elif oper == "%":
    result = n1 % n2
    print(f"{n1} {oper} {n2} = {result}")
else:
    if oper == "+":
        result = n1 + n2
    elif oper == "-":
        result = n1 - n2
    else:
        result = n1 * n2
    print(f"{n1} {oper} {n2} = {result} - {'even' if result % 2 == 0 else 'odd'}")
