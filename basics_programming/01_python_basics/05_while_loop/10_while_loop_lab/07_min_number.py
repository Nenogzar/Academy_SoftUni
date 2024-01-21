min_number = float("inf")

while True:
    user_input = input()

    if user_input == "Stop":
        break

    number = int(user_input)
    min_number = min(min_number, number)
print(min_number)
