def operation_multiply(num1, num2):
    operation = num1 * num2
    return operation

def operation_divide(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero!")

    else:
        operation = num1 / num2
        return operation

def operation_add(num1, num2):
    operation = num1 + num2
    return operation

def operation_subtract(num1, num2):
    operation = num1 - num2
    return operation

def calculation(operator, num1, num2):  # Подадени аргументи на функцията
    if operator.lower() == "multiply":
        print(f"{operation_multiply(num1, num2):.0f}")
    elif operator.lower() == "divide":
        print(f"{operation_divide(num1, num2):.0f}")
    elif operator.lower() == "add":
        print(f"{operation_add(num1, num2):.0f}")
    elif operator.lower() == "subtract":
        print(f"{operation_subtract(num1, num2):.0f}")
    else:
        print("Wrong command!")

def main():
    operator = input()
    num1 = int(input())
    num2 = int(input())
    calculation(operator, num1, num2)

if __name__ == "__main__":
    main()
