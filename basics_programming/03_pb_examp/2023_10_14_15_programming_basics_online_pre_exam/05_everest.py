days = 1
min_height = 5_364
max_height = 8_848

while True:
    sleep_yes_or_no = input().strip().lower()

    if sleep_yes_or_no == "end":
        print("Failed!")
        #print(f"Total days: {days}")
        print(f"{min_height}")
        break

    try:
        claimed_distance = int(input())
    except ValueError:
        print(" ")          #  Проверка за вход
        continue

    if sleep_yes_or_no == "yes":
        days += 1
        min_height += claimed_distance
    else:
        min_height += claimed_distance

    if days > 5:
        min_height -= claimed_distance

    if min_height >= max_height:
        print(f"Goal reached for {days} days!")
        break

    if days > 5:
        print("Failed!")
        #print(f"{days}")               # всички дни
        print(f"{min_height}")          # финални метри
        break
