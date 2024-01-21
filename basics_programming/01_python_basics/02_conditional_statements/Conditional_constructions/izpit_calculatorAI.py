while True:
    # проверка за числа въведени от клавиатурата
    a_input = input("a =  ")
    b_input = input("b =  ")

    if not a_input.isdigit() or not b_input.isdigit():
        print("Моля, въведете валидни числови стойности.")
        continue
    a = float(a_input)
    b = float(b_input)

    operation = input("Изберете операция: Събиране(+), Изваждане(-), Умножение(*), Деление(/) и Модулно деление(%)")
    result = 0
    event = ""

    # Пресмятане
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if b == 0:
            print(f"Cannot divide {b} by zero")
            continue
        result = a / b
    elif operation == "%":
        if b == 0:
            print(f"Cannot divide {b} by zero")
            continue
        result = a % b
    else:
        print("Невалидна операция")
        continue

    event = result%2
    if event == 0:
        event = "event"
    else:
        event = "odd"


    if operation == "%":
        print(f"{int(a)} % {int(b)} = {result:.0f}")
    elif operation =="+" or operation == "-" or operation == "*":
        print(f"{int(a)} {operation} {int(b)} = {result:.0f} - {event}")
    else:
        print(f"{a} {operation} {b} = {result:.0f}")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
