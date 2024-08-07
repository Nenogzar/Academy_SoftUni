""" Time: 0.020 s """

number_of_pieces = int(input())
piece_info = {}


for song in range(number_of_pieces):
    info = input().split("|")
    piece, composer, key = info[0], info[1], info[2]
    piece_info[piece] = {'composer': composer, 'key':key}

command = input()
while command != "Stop":
    command = command.split("|")
    action, piece = command[0], command[1]
    if action == "Add":
        if piece in piece_info:
            print(f"{piece} is already in the collection!")
        else:
            composer, key = command[2], command[3]
            piece_info[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        if piece not in  piece_info:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del piece_info[piece]
            print(f"Successfully removed {piece}!")

    elif action == "ChangeKey":
        new_key = command[2]
        if piece not in piece_info:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            print(f"Changed the key of {piece} to {new_key}!")
            piece_info[piece]['key'] = new_key


    command = input()

for piece, detail in piece_info.items():
    print(f"{piece} -> Composer: {detail['composer']}, Key: {detail['key']}")


""" Time: 0.080 s """

from collections import defaultdict

def process_commands(command, composition):
    action, *args = command.split('|')
    if action == 'Add':
        piece, composer, key = args
        if piece not in composition:
            composition[piece]['composer'] = composer
            composition[piece]['key'] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == 'Remove':
        piece = args[0]
        if piece in composition:
            del composition[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == 'ChangeKey':
        piece, new_key = args
        if piece in composition:
            composition[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

composition = defaultdict(lambda: defaultdict(str))

number_of_pieces = int(input())
for _ in range(number_of_pieces):
    info_piece = input().split("|")
    piece, composer, key = info_piece[0], info_piece[1], info_piece[2]
    composition[piece]['composer'] = composer
    composition[piece]['key'] = key

commands = input()
while commands != "Stop":
    process_commands(commands, composition)
    commands = input()

if composition:
    for piece, details in composition.items():
        print(f"{piece} -> Composer: {details['composer']}, Key: {details['key']}")
else:
    print("No pieces in the collection.")
