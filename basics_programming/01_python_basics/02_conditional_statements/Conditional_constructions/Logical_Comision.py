while True:
    city = input("Град: Sofia, Varna, Plovdiv: ")
    if city == "": #проверка за празна стойност
        continue
    revenue = input("Каква е печалбата? ")
    try:
        revenue = float(revenue)
    except ValueError:
        continue
    commission = 0.00
    if city == "Sofia":
        if 0 <= revenue <= 500:
            commission = revenue * 0.05
        elif 500 <= revenue <= 1000:
            commission = revenue * 0.07
        elif 1000 <= revenue <= 10000:
            commission = revenue * 0.08
        elif revenue > 10000:
            commission = revenue * 0.12
    elif city == "Varna":
        if 0 <= revenue <= 500:
            commission = revenue * 0.045
        elif 500 <= revenue <= 1000:
            commission = revenue * 0.75
        elif 1000 <= revenue <= 10000:
            commission = revenue * 0.10
        elif revenue > 10000:
            commission = revenue * 0.13
    elif city == "Plovdiv":
        if 0 <= revenue <= 500:
            commission = revenue * 0.055
        elif 500 <= revenue <= 1000:
            commission = revenue * 0.08
        elif 1000 <= revenue <= 10000:
            commission = revenue * 0.12
        elif revenue > 10000:
            commission = revenue * 0.145
    else:
        print("Града не е в списъка. Изберете из между Sofia, Varna, Plovdiv")
        continue

    if commission > 0:
        print(f" Комисионната за продажби на стойност {revenue}лв. в гр.{city} e {commission:.2f}лв.")
    else:
        print(f"Комисионна за продажби на стойност { revenue}лв. в гр.{city} не се полага!")

    repeat = input("Искате ли да повторите (Y/N)? ")
    if repeat.upper() == "N":
        print("Благодаря!")
        break
