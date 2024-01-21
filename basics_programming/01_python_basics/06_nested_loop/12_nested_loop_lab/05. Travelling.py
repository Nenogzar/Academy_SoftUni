saved_money = 0

while True:
    destination = input()

    if destination == 'End':
        break

    budget = float(input())
    saved_money = 0

    while saved_money < budget:
        saved = float(input())
        saved_money += saved

    print(f'Going to {destination}!')