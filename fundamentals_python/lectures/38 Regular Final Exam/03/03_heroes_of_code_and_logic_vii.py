number_of_heroes = int(input())
hero = {}

for _ in range(number_of_heroes):
    hero_info = input().split(" ")
    hero_name, hp, mp = hero_info[0], int(hero_info[1]), int(hero_info[2])

    max_hp = 100
    max_mp = 200

    if hero_name in hero:
        hero[hero_name]['hp'] = hp
        hero[hero_name]['mp'] = mp
    else:
        hero[hero_name] = {
            'hp': hp,
            'mp': mp
        }

command = input()

while command != "End":
    split_command = command.split(" - ")
    action, hero_name = split_command[0], split_command[1]

    if action == "CastSpell":
        MP_needed, spell_name = int(split_command[2]), split_command[3]
        if hero[hero_name]['mp'] >= MP_needed:
            hero[hero_name]['mp'] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage, attacker = int(split_command[2]), split_command[3]
        hero[hero_name]['hp'] -= damage
        if hero[hero_name]['hp'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero[hero_name]['hp']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del hero[hero_name]

    elif action == "Recharge":
        amount = int(split_command[2])
        recovered_amount = amount
        hero[hero_name]['mp'] += amount
        if hero[hero_name]['mp'] > max_mp:
            recovered_amount = amount - (hero[hero_name]['mp'] - max_mp)
            hero[hero_name]['mp'] = max_mp
        print(f"{hero_name} recharged for {recovered_amount} MP!")

    elif action == "Heal":
        amount = int(split_command[2])
        recovered_amount = amount
        hero[hero_name]['hp'] += amount
        if hero[hero_name]['hp'] > max_hp:
            recovered_amount = amount - (hero[hero_name]['hp'] - max_hp)
            hero[hero_name]['hp'] = max_hp
        print(f"{hero_name} healed for {recovered_amount} HP!")

    command = input()

for hero_name, details in hero.items():
    print(f"{hero_name}\n  HP: {details['hp']}\n  MP: {details['mp']}")
