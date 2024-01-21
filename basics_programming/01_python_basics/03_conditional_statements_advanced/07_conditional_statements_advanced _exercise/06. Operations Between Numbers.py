n1 = int(input())
n2 = int(input())
oper = input()
result = 0
type = ""

if oper == "+" or oper == "*" or oper == "-":
    if oper == "+":
        result = n1 + n2
    elif oper == "*":
        result = n1 * n2
    else:
        result = n1 - n2

    if result % 2 == 0:
        type = "even"
    else:
        type = "odd"
    print(f"{n1} {oper} {n2} = {result} - {type}")
elif oper == "/" or oper == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        if oper == "/":
            result = n1 / n2
            print(f"{n1} / {n2} = {result:.2f}")
        else:
            result = n1 % n2
            print(f"{n1} % {n2} = {result:.0f}")