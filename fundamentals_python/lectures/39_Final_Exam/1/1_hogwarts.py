spell = input()

possible_commands = input()
while possible_commands != "Abracadabra":
    split_command = possible_commands.split(" ")
    action = split_command[0]

    if action == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif action == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif action == "Illusion":
        index, letter = int(split_command[1]), split_command[2]
        if 0 <= index < len(spell):
            spell = spell[:index] + letter + spell[index + 1:]
            print("Done!")
        else:
            print("The spell was too weak.")
    elif action == "Divination":
        f_substring, s_substring = split_command[1], split_command[2]
        if f_substring not in spell:
            continue
        else:
            spell = spell.replace(f_substring, s_substring)
            print(spell)

    elif action == "Alteration":
        substring = split_command[1]
        if substring not in spell:
            continue
        else:
            spell = spell.replace(substring, '')

        print(spell)
    else:
        print("The spell did not work!")

    possible_commands = input()
