while True:
    a = float(input())
    b = float(input())
    operation = input("Изберете операция: Събиране(+), Изваждане(-), Умножение(*), Деление(/) и Модулно деление(%)")
    result = 0
    chetno = int(a) % 2

    if chetno == 0:
        chetno = "even"
    elif chetno == 1:
        chetno = "odd"
    else:
        chetno = ""

    # Пресмятане
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    print(f"{a} {operation} {b} = {result:.2f} - {chetno}")

    if operation == "/":
        if a == 0 or b == 0:
            print(f"Cannot divide {a} by {b} because a or b is equal to 0")
            continue
        else:
            result = a / b
        print(f"{a} / {b} = {result:.2f}")

    if operation == "%":
        result = a % b
        print(f"{a} % {b} = {result:.1f}")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
