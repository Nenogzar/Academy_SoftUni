command = input()
num = input()

if command == "int":
    result = int(num) * 2
elif command == "real":
    result = f"{float(num) * 1.5:.2f}"
elif command == "string":
    result = f"${num}$"

print(result)


""" 2 """

command = input()
to_process = input()


def calculate(command, calculation):
    result = ""
    if command == "int":
        result = f"{int(calculation) * 2:.0f}"
    elif command == "real":
        result = f"{float(calculation) * 1.5:.2f}"
    elif command == "string":
        result = "$" + calculation + "$"
    return result


print(calculate(command, to_process))


"""3 """
command = input()
number = input()


def calc(arg1, arg2):
    if arg1 == "int":
        result = float(arg2) * 2
        return f"{result:.0f}"

    elif arg1 == "real":
        result = float(arg2) * 1.5
        return f"{result:.2f}"

    elif arg1 == "string":
        return f"${arg2}$"


print(calc(command, number))


