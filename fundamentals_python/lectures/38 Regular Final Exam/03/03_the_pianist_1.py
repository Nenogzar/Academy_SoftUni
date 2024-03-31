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
