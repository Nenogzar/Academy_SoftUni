deposited_amount = float(input("Въведете депозираната сума: "))
deposit_period = int(input("Въведете срок на депозита (в месеци): "))
annual_interest_rate = float(input("Въведете лихвен процент: "))

monthly_interest_rate = annual_interest_rate / 100 / 12 # Годишен лихвен процент
total_amount = deposited_amount + deposit_period * ((deposited_amount * monthly_interest_rate)) #

print(f"Сумата в края на срока е: {total_amount:.2f}")
