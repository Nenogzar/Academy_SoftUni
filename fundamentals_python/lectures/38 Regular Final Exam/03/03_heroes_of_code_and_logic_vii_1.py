from collections import defaultdict


def add_hero(hero_name, hp, mp, hero_dict):
    hero_dict[hero_name]['hp'] = hp
    hero_dict[hero_name]['mp'] = mp


def Cast_Spell(hero_name, mp, spell_name, hero_dict):
    if hero_dict[hero_name]['mp'] < mp:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    else:
        hero_dict[hero_name]['mp'] -= mp
        print(f"{hero_name} has successfully cast {spell_name} and now has {hero_dict[hero_name]['mp']} MP!")


def Take_Damage(hero_name, damage, attaker_name, hero_dict):
    take_damage = hero_dict[hero_name]['hp'] - damage
    if take_damage > 0:
        hero_dict[hero_name]['hp'] -= damage
        print(
            f"{hero_name} was hit for {damage} HP by {attaker_name} and now has {hero_dict[hero_name]['hp']} HP left!")
    else:
        print(f"{hero_name} has been killed by {attaker_name}!")
        del hero_dict[hero_name]


def Recharge_MP(hero_name, amount, max_mp, hero_dict):
    current_mp = hero_dict[hero_name]['mp'] + amount
    if current_mp >= max_mp:
        amount_recovered = max_mp - hero_dict[hero_name]['mp']
        hero_dict[hero_name]['mp'] = max_mp
    else:
        hero_dict[hero_name]['mp'] += amount
        amount_recovered = amount
    print(f"{hero_name} recharged for {amount_recovered} MP!")


def Heal_HP(hero_name, amount, max_hp, hero_dict):
    current_hp = hero_dict[hero_name]['hp'] + amount
    if current_hp >= max_hp:
        amount_recovered = max_hp - hero_dict[hero_name]['hp']
        hero_dict[hero_name]['hp'] = max_hp
    else:
        amount_recovered = amount
        hero_dict[hero_name]['hp'] += amount

    print(f"{hero_name} healed for {amount_recovered} HP!")


def process_command(different_command, hero_dict):
    action, hero_name = different_command.split(" - ")[0], different_command.split(" - ")[1]
    if action == "CastSpell":
        mp, spell_name = int(different_command.split(" - ")[2]), different_command.split(" - ")[3]
        Cast_Spell(hero_name, mp, spell_name, hero_dict)
    elif action == "TakeDamage":
        damage, attaker_name = int(different_command.split(" - ")[2]), different_command.split(" - ")[3]
        Take_Damage(hero_name, damage, attaker_name, hero_dict)

    elif action == "Recharge":
        max_mp = 200
        amount = int(different_command.split(" - ")[2])
        Recharge_MP(hero_name, amount, max_mp, hero_dict)

    elif action == "Heal":
        max_hp = 100
        amount = int(different_command.split(" - ")[2])
        Heal_HP(hero_name, amount, max_hp, hero_dict)


hero_dict = defaultdict(lambda: {'hp': 0, 'mp': 0})
number_of_heroes = int(input())

for name in range(number_of_heroes):
    info_hero = input().split(" ")
    hero_name, hp, mp = info_hero[0], int(info_hero[1]), int(info_hero[2])
    add_hero(hero_name, hp, mp, hero_dict)

different_command = input()
while different_command != "End":
    process_command(different_command, hero_dict)
    different_command = input()

for hero, items in hero_dict.items():
    print(f"{hero}\n  HP: {items['hp']}\n  MP: {items['mp']} ")
