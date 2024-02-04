def create_bar(percentage_fill: int):
    percentage_fill //= 10

    perc_symbols = "%" * percentage_fill
    dot_symbols = "." * (10 - len(perc_symbols))

    return f"[{perc_symbols}{dot_symbols}]"


def display_result(percentage_fill: int):
    result = []
    bar = create_bar(percentage_fill)

    if percentage_fill == 100:
        result.append("100% Complete!")
        result.append(bar)

    elif percentage_fill != 100:
        result.append(f"{percentage_fill}% {bar}")
        result.append("Still loading...")

    return "\n".join(result)


percentage = int(input())
print(display_result(percentage))

""" 2 """
number = int(input())


def loading_bar(num):
    num_range = int(num / 10)
    target = 10
    if target == num_range:
        return "100% Complete!\n" + "[" + target * "%" + "]"
    else:
        return f"{num}% " + "[" + num_range * "%" + (target - num_range) * "." + "]\n" + "Still loading..."


print(loading_bar(number))

""" 3 """
