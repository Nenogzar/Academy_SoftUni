city = input().capitalize()
sales_volume = float(input()) #Обем на продажбите

# Проверка за валиден град и обем на продажбите
if city == "Sofia":
    if 0 <= sales_volume <= 500:
        commission_rate = 0.05
    elif 500 < sales_volume <= 1000:
        commission_rate = 0.07
    elif 1000 < sales_volume <= 10000:
        commission_rate = 0.08
    elif sales_volume > 10000:
        commission_rate = 0.12
    else:
        print("error")
        exit(1)
elif city == "Varna":
    if 0 <= sales_volume <= 500:
        commission_rate = 0.045
    elif 500 < sales_volume <= 1000:
        commission_rate = 0.075
    elif 1000 < sales_volume <= 10000:
        commission_rate = 0.10
    elif sales_volume > 10000:
        commission_rate = 0.13
    else:
        print("error")
        exit(1)
elif city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        commission_rate = 0.055
    elif 500 < sales_volume <= 1000:
        commission_rate = 0.08
    elif 1000 < sales_volume <= 10000:
        commission_rate = 0.12
    elif sales_volume > 10000:
        commission_rate = 0.145
    else:
        print("error")
        exit(1)
else:
    print("error")
    exit(1)

# Изчисляване на комисионната
commission = sales_volume * commission_rate
print(f"{commission:.2f}")
