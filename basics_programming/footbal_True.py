while True:
    budjet_str = input("Бюджет: ")
    if not budjet_str:
        repeat = input("Въведете Бюджет Y/N")
        if repeat.upper() == "N":
            print("10x")
            break
    budjet = float(budjet_str)
    category = input("VIP or Normal: ")
    fans_str = input("Колко фена: ")
    if not fans_str:
        repeat = input("Въведете брой на фенове, Y/N")
        if repeat.upper() == "N":
            print("10x")
            break
    fans = int(fans_str)
    spend = 0.00
    transport = budjet * 0.25
    if 0 < fans <= 4:
        transport = budjet * 0.75
    elif 5 <= fans <= 9:
        transport = budjet * 0.60
    elif 10 <= fans <= 24:
        transport = budjet * 0.50
    elif 25 <= fans <= 49:
        transport = budjet * 0.40
    else:
        print("Липсва брой фенове:")
        repeat = input("Y/N")
        if repeat.upper() == "N":
            print("10x")
            break
    if not break_flag:
        tickets_budjet = budjet - transport

        if category == "VIP":
            need_budjet = fans * 499.99
        else:
            need_budjet = fans * 249.99

        spend = tickets_budjet - need_budjet
        if spend < 0:
            print(f"Not enough money! You need {abs(spend):.2f} leva.")
        else:
            print(f"Yes! You have {spend:.2f} leva left.")
