while True:

    flowers_type = input("Roses, Dahlias, Tulips, Narcissus или Gladiolus: ")
    flowers_count = int(input("Колко цветя искате: "))
    budget = float(input("С какъв бюджет разполагате? "))
    Roses = 5
    Dahlias = 3.80
    Tulips = 2.80
    Narcissus = 3
    Gladiolus = 2.50
    money_need = 0.00
    balance = 0.00

    if flowers_type == "Roses":
        money_need = Roses * flowers_count
    elif flowers_type == "Dahlias":
        money_need = Dahlias * flowers_count
    elif flowers_type == "Tulips":
        money_need = Tulips * flowers_count
    elif flowers_type == "Narcissus":
        money_need = Narcissus * flowers_count
    elif flowers_type == "Gladiolus":
        money_need = Gladiolus * flowers_count
    else:
        print("Няма такова цвете в асортимента!")
        continue


    # Отстъпки
    if flowers_count > 80 and flowers_type == "Roses":
        balance = budget - money_need*0.9
    elif flowers_count > 90 and flowers_type == "Dahlias":
        balance = budget - money_need*0.85
    elif flowers_count >80 and flowers_type == "Tulips":
        balance = budget - money_need*0.85
    elif flowers_count < 120 and flowers_type == "Narcissus":
        balance = budget - money_need*1.15
    elif flowers_count < 80 and flowers_type =="Gladiolus":
        balance = budget - money_need*1.20
    else:
        balance = budget - money_need

    if balance > budget:
        print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {balance:.2f} leva left.")
    else:
        print(f"Not enough money, you need {balance:.2f} leva more.")



    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
