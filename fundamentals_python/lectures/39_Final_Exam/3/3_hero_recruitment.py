receiving_commands = input()
heroes_info = {}

while receiving_commands != "End":
    info = receiving_commands.split(" ")
    action, hero_name = info[0], info[1]

    if action == "Enroll":
        if hero_name not in heroes_info:
            heroes_info[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif action == "Learn":
        spell = info[2]

        if hero_name in heroes_info:
            if spell not in heroes_info[hero_name]:
                heroes_info[hero_name].append(spell)
            else:
                print(f"{hero_name} has already learnt {spell}.")
        else:
            print(f"{hero_name} doesn't exist.")

    elif action == "Unlearn":
        spell = info[2]

        if hero_name in heroes_info:

            if spell in heroes_info[hero_name]:
                heroes_info[hero_name].remove(spell)
            else:
                print(f"{hero_name} doesn't know {spell}.")
        else:
            print(f"{hero_name} doesn't exist.")
    # else:
    #     print("Invalid command.")

    receiving_commands = input()


print("Heroes:")
for hero, spells in heroes_info.items():
    print(f"== {hero}: {', '.join(spells)}")
