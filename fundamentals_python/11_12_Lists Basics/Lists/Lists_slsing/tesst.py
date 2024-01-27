energy = 100
coins = 100
events = input()
fail = False
value = 0
events_list = events.split('|')
commands_list = []
for char in events_list:
    commands_list = char.split('-')
    if commands_list[0] == 'rest':
        value = int(commands_list[1])
        energy += value
        if energy > 100:
            value = int(commands_list[1]) - (energy - 100)
            energy = 100
        print(f'You gained {value} energy.\n'
        f'Current energy: {energy}.')
    elif commands_list[0] == 'order':
        energy -= 30
        if energy >= 0:
            value = int(commands_list[1])
            coins += value
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print('You had to rest!')
            continue
    else:
        value = int(commands_list[1])
        if coins - value >= 0:
            coins -= value
            print(f'You bought {commands_list[0]}.')
        else:
            print(f'Closed! Cannot afford {commands_list[0]}.')
            fail = True
            break
if fail is False:
    print(f'Day completed!\n'
          f'Coins: {coins}\n'
          f'Energy: {energy}')